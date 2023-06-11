from flask import Flask, render_template, request
import folium
import pandas as pd
from pytrends.request import TrendReq
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        palavra_chave = request.form['palavra_chave']
        
        # Criar o mapa
        m = folium.Map(location=[-29.258165, -51.528917], zoom_start=7)
       
        # Adicionar marcador
        folium.Marker(
            location=[-29.258165, -51.528917],
            popup='Colonia de Conde DEu',
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
        # Adicionar marcador
        folium.Marker(
            location=[-29.177980890208307, -51.541576068166215],
            popup='Colonia de Dona Isabel',
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
        
        
        # Adicionar marcador
        folium.Marker(
            location=[-20.105142042681567, -40.528411191603865],
            popup='Colonia de Santa Leopoldina',
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)

        # Faz a pesquisa na API do Google Trends
        pytrends = TrendReq(hl='pt-BR', tz=360)
        pytrends.build_payload(kw_list=[palavra_chave], geo='BR')
        dados = pytrends.interest_by_region(resolution='REGION', inc_low_vol=True, inc_geo_code=True)
        if dados.empty or dados[palavra_chave].sum() == 0:
            mensagem = f'Não há dados disponíveis para a pesquisa da palavra-chave "{palavra_chave}"'
            return render_template('index.html', mensagem=mensagem)

        # Cria o DataFrame a partir dos dados
        df = dados.reset_index()
        df.rename(columns={'geoCode': 'sigla'}, inplace=True)

        # Modifica a coluna 'sigla' mantendo apenas as duas últimas letras
        df['sigla'] = df['sigla'].str[-2:]
        
        if df.empty or df[palavra_chave].sum() == 0:
            # Caso o DataFrame esteja vazio ou todos os resultados sejam zero,
            # modificar a cor do mapa para vermelho
            fill_color = 'red'
            bins = [0]
        else:
            fill_color = 'YlGnBu'
            bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, df[palavra_chave].max()]

        # Adiciona os dados ao mapa
        choropleth = folium.Choropleth(
            geo_data='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson',
            name='choropleth',
            data=df,
            columns=['sigla', palavra_chave],
            key_on='feature.properties.sigla',
            fill_color=fill_color,
            fill_opacity=0.9,
            line_opacity=0.2,
            legend_name='Popularidade de busca por ' + palavra_chave + ' no Google Trends',
            nan_fill_color='YlOrRd',
            bins=bins,
            highlight=True,
            show=True,
            reset=True,
        ).add_to(m)

        # Função para adicionar informações ao tooltip de cada região
        def add_tooltip(row):
            sigla = row['sigla']
            popularidade = row[palavra_chave]
            tooltip_text = f'Estado: {sigla}<br>Popularidade: {popularidade}'
            folium.features.Tooltip(tooltip_text).add_to(choropleth.geojson)

        # Aplicar a função a cada linha do DataFrame
        df.apply(add_tooltip, axis=1)
        
        # Adiciona rótulos ao passar o mouse
        folium.features.GeoJsonTooltip(
            fields=['name'],
            aliases=['Estado:'],
            labels=True,
            localize=True,
            sticky=False
        ).add_to(choropleth.geojson)

        # Adiciona a camada de controle ao mapa
        folium.LayerControl(collapsed=True).add_to(m)

        # Renderizar o mapa para um arquivo HTML
        map_html = m.get_root().render()

        return render_template('index.html', map=map_html, palavra_chave=palavra_chave)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


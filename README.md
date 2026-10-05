# Abogados en Puerto Montt — rediseño

Propuesta de rediseño de https://www.abogadosenpuertomontt.cl (Estudio Calixto & Cía.).

## Estructura del sitio
Es un sitio estático de varias páginas, sin dependencias:

| URL | Contenido |
|---|---|
| `/` | Inicio: hero, servicios, cómo trabajamos y quiénes somos (resumen) |
| `/servicios/` | Todos los servicios + preguntas frecuentes |
| `/portfolio-item/<servicio>/` | Una página por servicio, con formulario lateral y FAQ |
| `/quienes-somos/` | Estudio, credenciales, equipo y cobertura |
| `/blog/` | Artículos del blog |
| `/contacto/` | Datos, mapa y formulario completo |
| `/ubicaciones/` | Redirige a `/contacto/` (URL del sitio antiguo) |
| `/404.html` | Página no encontrada |

Las páginas de servicio, `/servicios/`, `/quienes-somos/` y `/contacto/` usan **las mismas URLs del sitio actual** para conservar el posicionamiento en Google. También se generan `sitemap.xml` y `robots.txt`.

## Cómo editar
Las páginas HTML se **generan** con `build/build.py`. Los textos, servicios, equipo, blog y datos de contacto están al inicio de ese archivo. Después de editarlo, ejecuta:

```bash
python3 build/build.py
```

- Estilos: `assets/css/styles.css`. Los colores de marca están en `:root`.
- Comportamiento: `assets/js/main.js` (WhatsApp, formularios, menú, animaciones, horario).
- Íconos: `build/sprite.html`.

## Ver el sitio en local
```bash
python3 -m http.server 8000
```
Luego abre http://localhost:8000. Usa el servidor y no abras los archivos con doble clic, porque los enlaces a carpetas como `servicios/` necesitan un servidor.

## Objetivo principal
El sitio recibe tráfico de Google Ads, así que su meta es **convertir visitas en contactos para agendar una consulta**,
sobre todo por WhatsApp y llamada. Por eso:

- Hay botones de WhatsApp con mensaje ya escrito en el header, el hero, cada servicio, la sección de contacto y el cierre. También hay un botón flotante en escritorio y una barra fija con Llamar/WhatsApp en móvil.
- Los formularios (en el hero y en contacto) arman un mensaje con nombre, teléfono, materia y caso, y lo abren en WhatsApp, o por correo si la persona lo prefiere. No necesitan servidor.
- Cada clic en WhatsApp, llamada o correo, y cada envío de formulario, se registra como evento en `gtag`/`dataLayer` cuando Google Ads/GA4 está instalado. Eventos: `click_whatsapp`, `click_llamada`, `click_correo` y `envio_formulario`.
- Incluye SEO local: datos estructurados `LegalService`, title y description, y Open Graph.

## Pendientes antes de publicar
1. **Logo**: ya integrado (`assets/logo.png`, colores de marca #1B3263 / #686868). Si el estudio tiene una versión en mayor resolución o en SVG, conviene reemplazarla para que se vea más nítida en pantallas retina. El favicon (`assets/logo.svg`) es una recreación simple del monograma CC.
2. **Colores**: definidos en `:root` al inicio del `<style>`.
3. **Foto del abogado**: opcional, en la sección "Quiénes somos" (`.about-visual`).
4. **Etiqueta de Google Ads**: pegar el snippet `gtag` existente del sitio en el `<head>` y crear conversiones a partir de los eventos de arriba.
5. Revisar los textos con el estudio, incluida la lista de comunas de cobertura.
6. **Equipo**: confirmar nombres y cargos de E. Zapata y Roberto Calisto Villegas. Los obtuve de resultados de búsqueda, no del sitio.
7. **Blog**: las tarjetas enlazan a los artículos que ya existen en el sitio actual (WordPress). Si se reemplaza el WordPress, hay que migrar esos artículos o mantenerlos en sus mismas URLs.
8. **SEO**: las URLs de servicios ya coinciden con las actuales. Las páginas de laboral (`abogados-laborales-puerto-montt`) y herencias (`posesion-efectiva-puerto-montt`) son nuevas. Revisa en Google Search Console si existen otras URLs antiguas que haya que redirigir.
9. **Hosting**: el sitio funciona en cualquier hosting estático (Netlify, Vercel, GitHub Pages o el hosting actual). Hay que configurar `404.html` como página de error.

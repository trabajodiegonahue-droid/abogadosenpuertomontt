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
| `/AAAA/MM/DD/<artículo>/` | Cada artículo, en la misma URL que tiene hoy en WordPress |
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
Haz doble clic en **`ver-sitio.command`** (Mac) o en **`ver-sitio.bat`** (Windows). Trae los últimos cambios, levanta el servidor y abre el navegador.

También puedes hacerlo a mano:
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

## SEO
- Cada página tiene un solo `h1` con la palabra clave, y la jerarquía `h2` → `h3` no salta niveles. Los títulos de formularios y del pie no son encabezados.
- Títulos ≤ 60 caracteres y descripciones ≤ 155, todos únicos.
- Datos estructurados: `LegalService` (todas), `Service` (servicios), `FAQPage` (servicios y contacto) y `BreadcrumbList` (páginas internas).
- `canonical`, Open Graph con imagen de 1200×630 (`assets/og-image.png`), `sitemap.xml`, `robots.txt` y `noindex` en la 404.
- HTML validado sin errores.

## Pendientes antes de publicar
1. **Logo**: ya integrado (`assets/logo.png`, colores de marca #1B3263 / #686868). Si el estudio tiene una versión en mayor resolución o en SVG, conviene reemplazarla para que se vea más nítida en pantallas retina. El favicon (`assets/logo.svg`) es una recreación simple del monograma CC.
2. **Colores**: definidos en `:root` al inicio del `<style>`.
3. **Fotos**: no se pudieron descargar las imágenes del sitio actual (la red del entorno bloquea el dominio). Si el estudio las entrega (foto del abogado, oficina, equipo), se agregan en `assets/img/` y se integran en "Quiénes somos" y en el hero.
4. **Etiqueta de Google Ads**: pegar el snippet `gtag` existente del sitio en el `<head>` y crear conversiones a partir de los eventos de arriba.
5. Revisar los textos con el estudio, incluida la lista de comunas de cobertura.
6. **Equipo**: confirmar nombres y cargos de E. Zapata y Roberto Calisto Villegas. Los obtuve de resultados de búsqueda, no del sitio.
7. **Blog**: los 3 artículos ya son páginas del sitio nuevo, en sus mismas URLs. Su texto es un **borrador**: solo el primer párrafo del de precario es original; el resto se redactó a partir de la ley chilena. Hay que reemplazarlo por el texto original o revisarlo con el abogado. El blog actual tiene artículos más recientes que también hay que migrar (título, fecha, URL y texto), por ejemplo: "Juzgado de letras de Buin declara la nulidad absoluta de contratos de compraventa de inmueble", "Corte Suprema resuelve que negar prueba confesional en segunda instancia vulnera el derecho de defensa", "Corte Suprema resuelve que acción reivindicatoria procede contra mero tenedor", "Corte Suprema resuelve que acción de precario procede aunque la demanda no identifique con exactitud la parte ocupada" y "Proyecto de ley busca tipificar como delito el ingreso clandestino al territorio nacional".
10. **Redes sociales**: el sitio actual enlaza a Facebook, Instagram, LinkedIn, X, YouTube y Vimeo. Solo se conoce la URL de Facebook; hay que agregar las demás en `build/build.py`.
8. **SEO**: las URLs de servicios ya coinciden con las actuales. Las páginas de laboral (`abogados-laborales-puerto-montt`) y herencias (`posesion-efectiva-puerto-montt`) son nuevas. Revisa en Google Search Console si existen otras URLs antiguas que haya que redirigir.
9. **Hosting**: el sitio funciona en cualquier hosting estático (Netlify, Vercel, GitHub Pages o el hosting actual). Hay que configurar `404.html` como página de error.

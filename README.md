# Abogados en Puerto Montt — rediseño

Propuesta de rediseño de https://www.abogadosenpuertomontt.cl (Estudio Calixto & Cía.).
Página estática: `index.html` + `assets/`. Para verla, abre `index.html` en el navegador.

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

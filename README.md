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
1. **Logo oficial**: reemplazar `assets/logo.svg` (provisional) por el logo real y ajustar el `src` en `index.html`.
2. **Colores**: están definidos en `:root` al inicio del `<style>` (`--navy`, `--gold`). Hay que ajustarlos al logo oficial.
3. **Foto del abogado**: opcional, en la sección "Quiénes somos" (`.about-visual`).
4. **Etiqueta de Google Ads**: pegar el snippet `gtag` existente del sitio en el `<head>` y crear conversiones a partir de los eventos de arriba.
5. Revisar los textos con el estudio, incluida la lista de comunas de cobertura.

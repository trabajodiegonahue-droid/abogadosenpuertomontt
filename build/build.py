#!/usr/bin/env python3
"""Genera el sitio estático de Abogados en Puerto Montt (Estudio Calixto & Cía.).

Uso:  python3 build/build.py

Los datos (servicios, equipo, blog, contacto) están en este archivo. El encabezado,
el menú y el pie de página se comparten entre todas las páginas, así que cualquier
cambio se hace una sola vez aquí y se regenera todo el sitio.

Las páginas de servicio usan las mismas URLs que el sitio actual
(/portfolio-item/.../) para no perder el posicionamiento en Google.
"""
import os
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://www.abogadosenpuertomontt.cl"

PHONE = "+56 9 9797 9827"
PHONE_TEL = "+56997979827"
LANDLINE = "(65) 226 2388"
LANDLINE_TEL = "+56652262388"
EMAIL = "fcalixto.abogado@gmail.com"
ADDRESS = "Antonio Varas 216, Of. 309, Piso 3, Torre del Puerto, Puerto Montt"
HOURS = "Lunes a viernes · 09:00–13:00 y 15:00–18:30"
FACEBOOK = "https://www.facebook.com/abogados.ptomontt"
# Datos de confianza tomados del sitio y la ficha de Google del estudio (verificar antes de publicar)
RATING = "4,9"
REVIEWS = "433"
YEARS = "15"
GOOGLE_REVIEWS = "https://www.google.com/maps/search/?api=1&amp;query=Abogados%20en%20Puerto%20Montt%20Calixto%20%26%20C%C3%ADa"
SISTER_SITES = ["abogadosdepuertomontt.cl", "abogadosdepuertovaras.cl", "abogadoscalbuco.cl", "abogadoslosmuermos.cl", "defensaspuertomontt.cl"]

# ---------------------------------------------------------------------------
# Servicios
# ---------------------------------------------------------------------------
SERVICES = [
    {
        "slug": "abogados-de-familia-puerto-montt",
        "name": "Familia",
        "title": "Abogados de Familia en Puerto Montt",
        "card": "Abogados de Familia",
        "area": "Familia",
        "icon": "i-family",
        "sub": "Alimentos, divorcio, cuidado personal",
        "short": "Pensión de alimentos, divorcios, cuidado personal, relación directa y regular, y medidas de protección.",
        "lead": "Te asesoramos y representamos ante los Tribunales de Familia de Puerto Montt y la Región de Los Lagos, con cercanía y reserva en momentos difíciles.",
        "intro": "Los conflictos familiares requieren una asesoría que combine conocimiento técnico y sensibilidad. Te explicamos tus derechos, las alternativas de acuerdo y, si es necesario, defendemos tus intereses y los de tus hijos en juicio.",
        "items": [
            ("Pensión de alimentos", "Demanda, aumento, rebaja, cese y cobro de pensiones adeudadas."),
            ("Divorcio", "De mutuo acuerdo, unilateral o por culpa."),
            ("Cuidado personal", "Determinación o cambio de con quién viven los hijos."),
            ("Relación directa y regular", "Régimen de visitas y su cumplimiento."),
            ("Violencia intrafamiliar", "Medidas de protección y medidas cautelares urgentes."),
            ("Compensación económica", "Demanda o defensa en el marco del divorcio."),
        ],
        "callout": "En alimentos, cuidado personal y relación directa y regular, la ley exige por regla general una mediación previa antes de demandar. Te acompañamos también en esa etapa.",
        "faqs": [
            ("¿Cuánto tiempo de separación se necesita para divorciarse?", "Para el divorcio de mutuo acuerdo se exige, por regla general, al menos un año de cese de la convivencia; para el divorcio unilateral, al menos tres años. El divorcio por culpa no exige un plazo de separación."),
            ("¿Qué pasa si no me pagan la pensión de alimentos?", "Existen mecanismos de cobro como la liquidación de la deuda, la retención de remuneraciones, la inscripción en el Registro Nacional de Deudores de Pensiones de Alimentos y otras medidas de apremio. Te ayudamos a activarlos."),
            ("¿Puedo pedir medidas de protección con urgencia?", "Sí. Ante situaciones de violencia o riesgo, el tribunal puede decretar medidas cautelares de forma rápida. Escríbenos de inmediato para orientarte."),
        ],
    },
    {
        "slug": "abogados-de-divorcios-en-puerto-montt",
        "name": "Divorcios",
        "title": "Abogados de Divorcio en Puerto Montt",
        "card": "Divorcios",
        "area": "Divorcio",
        "icon": "i-rings",
        "sub": "Mutuo acuerdo, unilateral, por culpa",
        "short": "Divorcios de mutuo acuerdo, unilaterales y por culpa, compensación económica y liquidación de la sociedad conyugal.",
        "lead": "Tramitamos divorcios en Puerto Montt, Puerto Varas y comunas cercanas, con asesoría clara sobre plazos, bienes e hijos.",
        "intro": "Un divorcio implica decisiones importantes sobre los hijos, los bienes y el futuro de cada uno. Te explicamos qué tipo de divorcio corresponde a tu caso, buscamos acuerdos cuando es posible y te representamos ante el Tribunal de Familia.",
        "items": [
            ("Divorcio de mutuo acuerdo", "Cuando ambos están de acuerdo y hay al menos un año de cese de convivencia."),
            ("Divorcio unilateral", "Por cese de convivencia de al menos tres años."),
            ("Divorcio por culpa", "Por faltas graves a los deberes del matrimonio."),
            ("Compensación económica", "Para el cónyuge que se dedicó al cuidado de los hijos o del hogar."),
            ("Separación judicial", "Cuando no se busca terminar el matrimonio."),
            ("Separación de bienes", "Y liquidación de la sociedad conyugal."),
        ],
        "callout": "En el divorcio de mutuo acuerdo se presenta un acuerdo completo y suficiente que regula alimentos, cuidado personal y relación directa y regular de los hijos, además de las relaciones patrimoniales. Te ayudamos a redactarlo.",
        "faqs": [
            ("¿Cuánto demora un divorcio?", "Depende del tipo de divorcio y de si hay acuerdo. El de mutuo acuerdo suele ser el más rápido. En la primera consulta te damos una estimación para tu caso."),
            ("¿Cómo acredito el cese de la convivencia?", "Se puede acreditar con distintos medios, como un acuerdo de cese por escritura pública o acta, la demanda de separación, testigos u otros antecedentes. Revisamos cuáles tienes."),
            ("¿Qué pasa con los bienes al divorciarse?", "Depende del régimen matrimonial. Si están casados en sociedad conyugal, se debe liquidar. Te asesoramos en ese proceso."),
        ],
    },
    {
        "slug": "abogados-penalistas-puerto-montt",
        "name": "Penal",
        "title": "Abogados Penalistas en Puerto Montt",
        "card": "Defensa Penal",
        "area": "Penal",
        "icon": "i-shield",
        "sub": "Detenciones, formalización, juicio oral",
        "short": "Defensa en todo el proceso penal: Fiscalía, Juzgado de Garantía, Tribunal Oral y Cortes. También querellas para víctimas.",
        "lead": "Defensa penal privada en Puerto Montt y la Región de Los Lagos: desde el control de detención hasta el juicio oral y los recursos ante las Cortes.",
        "intro": "En materia penal, los primeros momentos son decisivos. Actuamos con rapidez para proteger tus derechos, revisar la legalidad de la detención y definir la mejor estrategia de defensa. También representamos a víctimas que necesitan presentar una querella.",
        "items": [
            ("Control de detención", "Asistencia urgente en la primera audiencia."),
            ("Formalización y cautelares", "Defensa frente a prisión preventiva y otras medidas."),
            ("Salidas alternativas", "Suspensión condicional y acuerdos reparatorios."),
            ("Juicio oral y abreviado", "Preparación y litigación ante el Tribunal Oral en lo Penal."),
            ("Recursos", "Apelaciones y nulidad ante las Cortes de Apelaciones y Suprema."),
            ("Querellas", "Representación de víctimas de delitos."),
        ],
        "callout": "Si tú o un familiar fue detenido, llámanos de inmediato: la persona debe ser puesta a disposición del Juzgado de Garantía dentro de las 24 horas siguientes, y contar con defensa desde esa audiencia hace la diferencia.",
        "faqs": [
            ("¿Qué hago si detuvieron a un familiar?", "Mantén la calma, no entregues declaraciones sin asesoría y contáctanos de inmediato al " + PHONE + ". Coordinaremos la defensa para la audiencia de control de detención."),
            ("¿Qué es la formalización?", "Es la comunicación que hace el fiscal, en presencia del juez de garantía, de que se está desarrollando una investigación en tu contra por uno o más delitos. Desde ese momento es clave contar con un abogado defensor."),
            ("¿Pueden representarme si soy víctima?", "Sí. Podemos presentar una querella y participar activamente en la investigación y el juicio para resguardar tus derechos."),
        ],
    },
    {
        "slug": "abogados-civiles-puerto-montt",
        "name": "Civil",
        "title": "Abogados Civiles en Puerto Montt",
        "card": "Juicios Civiles",
        "area": "Civil",
        "icon": "i-scale",
        "sub": "Tierras, precario, arriendos, cobranzas",
        "short": "Juicios de tierras, precario, desalojos, arriendos, indemnizaciones y cobranzas.",
        "lead": "Representación en juicios civiles en Puerto Montt, Puerto Varas y comunas cercanas: propiedades, arriendos, contratos e indemnizaciones.",
        "intro": "Asesoramos a personas y empresas en conflictos sobre bienes, contratos y obligaciones. Analizamos la documentación, buscamos primero una solución eficiente y, cuando corresponde, llevamos el caso a tribunales.",
        "items": [
            ("Juicios de tierras", "Deslindes, servidumbres y conflictos de propiedad."),
            ("Precario y reivindicación", "Recuperación de inmuebles ocupados sin título."),
            ("Arriendos", "Término de contrato, desalojo y cobro de rentas."),
            ("Indemnización de perjuicios", "Daños contractuales y extracontractuales."),
            ("Cobranzas", "Cobro judicial de pagarés, cheques y facturas."),
            ("Asuntos inmobiliarios", "Estudio de títulos y regularización de propiedades."),
        ],
        "callout": "La acción de precario permite recuperar un inmueble ocupado por alguien sin contrato ni título que lo justifique, incluso si se trata de un familiar o conocido.",
        "faqs": [
            ("¿Cómo recupero una propiedad ocupada sin permiso?", "Dependiendo del caso, puede proceder una acción de precario, reivindicatoria o de término de arriendo. Revisamos tus antecedentes y te recomendamos la vía más rápida."),
            ("¿Qué hago si mi arrendatario no paga?", "Podemos iniciar la acción de término de contrato y cobro de rentas, incluidos los procedimientos más breves que contempla la ley para estos casos."),
            ("¿Cuánto demora un juicio civil?", "Depende del tipo de procedimiento y de la defensa de la contraparte. En la primera consulta te damos una estimación realista para tu caso."),
        ],
    },
    {
        "slug": "asesoria-bienes-raices-puerto-montt",
        "name": "Inmobiliario",
        "title": "Abogados Inmobiliarios en Puerto Montt",
        "card": "Bienes Raíces",
        "area": "Bienes raíces",
        "icon": "i-key",
        "sub": "Estudio de títulos, compraventas, subdivisiones",
        "short": "Estudio de títulos, compraventas, arriendos y subdivisiones de propiedades urbanas y rurales.",
        "lead": "Asesoría legal inmobiliaria en Puerto Montt, Puerto Varas, Los Muermos, Calbuco y Maullín para comprar, vender o regularizar tu propiedad con seguridad.",
        "intro": "Comprar o vender una propiedad es una de las decisiones económicas más importantes. Revisamos los títulos, detectamos riesgos y redactamos los contratos para que la operación sea segura.",
        "items": [
            ("Estudio de títulos", "De propiedades urbanas y rurales antes de comprar o hipotecar."),
            ("Compraventas", "Redacción de promesas y escrituras de compraventa."),
            ("Arriendos", "Contratos habitacionales y comerciales."),
            ("Subdivisiones", "De predios rurales y urbanos."),
            ("Regularización", "De títulos y propiedades con problemas de inscripción."),
            ("Asesoría a inversionistas", "Para compras de parcelas, locales y propiedades en el sur."),
        ],
        "callout": "Antes de pagar un pie o firmar una promesa, pide un estudio de títulos: revisa la historia del dominio y la existencia de hipotecas, embargos, prohibiciones o litigios sobre la propiedad.",
        "faqs": [
            ("¿Qué es un estudio de títulos?", "Es la revisión legal de los antecedentes de una propiedad, normalmente de al menos los últimos diez años, para confirmar que el vendedor es dueño y que no hay gravámenes, prohibiciones ni litigios que afecten la compra."),
            ("¿Pueden ayudarme a comprar una parcela?", "Sí. Revisamos los títulos, la subdivisión y los permisos, y redactamos la promesa y la compraventa."),
        ],
    },
    {
        "slug": "defensas-laborales",
        "name": "Laboral",
        "title": "Abogados Laborales en Puerto Montt",
        "card": "Derecho Laboral",
        "area": "Laboral",
        "icon": "i-brief",
        "sub": "Despidos, indemnizaciones, accidentes",
        "short": "Despido injustificado, nulidad del despido, indemnizaciones y accidentes del trabajo. Para trabajadores y empleadores.",
        "lead": "Asesoría y juicios laborales para trabajadores y empleadores en Puerto Montt y la Región de Los Lagos.",
        "intro": "Si fuiste despedido, te deben cotizaciones o sufriste un accidente laboral, revisamos tu caso y te decimos qué puedes reclamar. A empleadores los asesoramos para prevenir conflictos y defenderlos en juicio.",
        "items": [
            ("Despido injustificado", "Cobro de indemnizaciones y recargos legales."),
            ("Nulidad del despido", "Cuando el empleador no pagó las cotizaciones."),
            ("Autodespido", "Despido indirecto por incumplimientos graves del empleador."),
            ("Accidentes del trabajo", "Indemnizaciones por accidentes del trabajo y enfermedades profesionales."),
            ("Tutela de derechos", "Vulneración de derechos fundamentales en el trabajo."),
            ("Asesoría a empleadores", "Contratos, reglamentos internos, despidos y finiquitos."),
        ],
        "callout": "Los plazos laborales son cortos: por regla general tienes 60 días hábiles desde el despido para demandar (90 si antes presentaste un reclamo en la Inspección del Trabajo). No esperes para consultar.",
        "faqs": [
            ("¿Debo firmar el finiquito?", "Antes de firmar, revisa que estén todos los montos. Si no estás de acuerdo, puedes firmar con reserva de derechos. Te ayudamos a revisarlo."),
            ("¿Qué es la nulidad del despido?", "Si tu empleador no pagó tus cotizaciones previsionales al momento del despido, este no produce efectos y puede quedar obligado a pagar las remuneraciones hasta que regularice esa situación."),
            ("¿También asesoran a empresas?", "Sí. Asesoramos a empleadores en contratos, reglamentos internos, terminaciones de contrato y defensa en juicios laborales."),
        ],
    },
    {
        "slug": "posesion-efectiva-puerto-montt",
        "name": "Herencias",
        "title": "Herencias y Posesión Efectiva en Puerto Montt",
        "card": "Herencias y Posesión Efectiva",
        "area": "Herencias / Posesión efectiva",
        "icon": "i-home",
        "sub": "Posesión efectiva, partición, testamentos",
        "short": "Tramitación de posesiones efectivas, partición de herencias y regularización de bienes heredados.",
        "lead": "Tramitamos posesiones efectivas y particiones de herencia en Puerto Montt para que puedas disponer legalmente de los bienes heredados.",
        "intro": "Cuando fallece un familiar, los herederos necesitan la posesión efectiva para poder vender, arrendar o repartir los bienes. Nos encargamos de todo el proceso y de las inscripciones posteriores.",
        "items": [
            ("Posesión efectiva intestada", "Tramitación ante el Registro Civil cuando no hay testamento."),
            ("Posesión efectiva testada", "Tramitación ante el tribunal cuando existe testamento."),
            ("Inscripciones", "Inscripción especial de herencia en el Conservador de Bienes Raíces."),
            ("Partición de herencia", "Acuerdo o juicio de partición entre herederos."),
            ("Impuesto a la herencia", "Orientación sobre la declaración ante el SII."),
            ("Regularización de bienes", "Vehículos, cuentas, inmuebles y otros bienes."),
        ],
        "callout": "La posesión efectiva es el primer paso: sin ella los herederos no pueden vender ni repartir legalmente los bienes del causante.",
        "faqs": [
            ("¿Dónde se tramita la posesión efectiva?", "Si no hay testamento, ante el Servicio de Registro Civil. Si hay testamento, ante el tribunal civil competente."),
            ("¿Qué documentos necesito?", "Por lo general, certificados de defunción, nacimiento o matrimonio que acrediten el parentesco, e información de los bienes. En la consulta te damos la lista exacta para tu caso."),
            ("¿Qué pasa si los herederos no se ponen de acuerdo?", "Se puede realizar una partición judicial ante un juez árbitro. Te representamos en ese proceso."),
        ],
    },
    {
        "slug": "abogados-policia-local-puerto-montt",
        "name": "Policía Local",
        "title": "Abogados de Policía Local en Puerto Montt",
        "card": "Policía Local",
        "area": "Policía Local",
        "icon": "i-car",
        "sub": "Choques, infracciones, consumidor",
        "short": "Accidentes de tránsito, indemnización de daños, infracciones y causas del consumidor.",
        "lead": "Defensa y demandas ante los Juzgados de Policía Local de Puerto Montt y comunas cercanas.",
        "intro": "Un choque o una infracción puede terminar en multas, suspensión de licencia o en una demanda por los daños. Te representamos para defenderte o para cobrar la indemnización que corresponde.",
        "items": [
            ("Accidentes de tránsito", "Defensa y demanda civil por daños al vehículo y lesiones."),
            ("Infracciones", "Defensa ante partes y denuncias."),
            ("Derechos del consumidor", "Reclamos y demandas contra empresas."),
            ("Daños y perjuicios", "Cobro de reparaciones, lucro cesante y daño moral."),
        ],
        "callout": "Después de un accidente, guarda fotos, datos del otro conductor, testigos y el parte o constancia policial. Son clave para tu defensa o tu demanda.",
        "faqs": [
            ("¿Necesito abogado para ir al Juzgado de Policía Local?", "No siempre es obligatorio, pero contar con uno mejora mucho tus posibilidades, sobre todo si quieres cobrar una indemnización o si arriesgas la suspensión de tu licencia."),
            ("¿Puedo cobrar los daños de mi vehículo?", "Sí. Junto con la denuncia se puede presentar una demanda civil para cobrar los daños y perjuicios causados."),
        ],
    },
    {
        "slug": "sociedades-y-empresas-puerto-montt",
        "name": "Sociedades",
        "title": "Sociedades y Empresas en Puerto Montt",
        "card": "Sociedades y Empresas",
        "area": "Sociedades y empresas",
        "icon": "i-building",
        "sub": "Constitución, modificaciones, pymes",
        "short": "Constitución y modificación de sociedades (también \"Empresa en un Día\") y asesoría permanente a pymes.",
        "lead": "Asesoría legal a emprendedores, pymes y empresas de Puerto Montt: desde la constitución de la sociedad hasta la gestión diaria.",
        "intro": "Te ayudamos a elegir el tipo de sociedad que más te conviene, la constituimos y te acompañamos con contratos, modificaciones y asesoría permanente para que tu negocio crezca sobre una base legal sólida. Contamos con apoyo contable para una mirada integral.",
        "items": [
            ("Constitución de sociedades", "SpA, EIRL, Limitada y otras formas societarias."),
            ("Empresa en un Día", "Constitución electrónica en el Registro de Empresas y Sociedades."),
            ("Modificaciones", "Ingreso o salida de socios, aumentos de capital y cambios de giro."),
            ("Disolución", "Término y liquidación ordenada de sociedades."),
            ("Contratos comerciales", "Compraventa, prestación de servicios, distribución y otros."),
            ("Asesoría permanente", "Acompañamiento legal mensual para pymes."),
        ],
        "callout": "El sistema \"Empresa en un Día\" permite constituir ciertas sociedades en forma electrónica y rápida. Te asesoramos para elegir entre esta vía y la constitución tradicional.",
        "faqs": [
            ("¿Qué tipo de sociedad me conviene?", "Depende del número de socios, el giro, la responsabilidad que quieras asumir y tus planes de crecimiento. Lo analizamos contigo en la primera consulta."),
            ("¿Pueden asesorar mi empresa de forma permanente?", "Sí. Ofrecemos asesoría legal continua para pymes y empresas, con apoyo contable cuando se requiere."),
        ],
    },
    {
        "slug": "redaccion-de-escrituras",
        "name": "Contratos",
        "title": "Escrituras y Contratos en Puerto Montt",
        "card": "Contratos y Escrituras",
        "area": "Contratos y escrituras",
        "icon": "i-doc",
        "sub": "Compraventas, arriendos, poderes",
        "short": "Redacción y revisión de escrituras públicas y privadas, compraventas, arriendos y contratos.",
        "lead": "Redactamos escrituras públicas y privadas en Puerto Montt, Puerto Varas, Los Muermos, Calbuco, Maullín y alrededores.",
        "intro": "Un contrato bien redactado evita conflictos futuros. Preparamos y revisamos tus documentos para que reflejen exactamente lo acordado y protejan tus intereses.",
        "items": [
            ("Compraventas", "De inmuebles, vehículos y otros bienes."),
            ("Promesas de compraventa", "Para asegurar la operación antes de firmar la escritura definitiva."),
            ("Contratos de arriendo", "Habitacionales y comerciales."),
            ("Mandatos y poderes", "Generales y especiales."),
            ("Servidumbres y cesiones", "Servidumbres de tránsito y cesiones de derechos."),
            ("Revisión de contratos", "Antes de firmar cualquier documento importante."),
        ],
        "callout": "Las escrituras públicas se firman ante notario, pero su contenido debe ser redactado y revisado por un abogado. Nosotros nos encargamos de ese trabajo.",
        "faqs": [
            ("¿Pueden revisar un contrato antes de que lo firme?", "Sí, y es lo más recomendable. Revisamos el documento y te explicamos sus riesgos antes de firmar."),
            ("¿Atienden fuera de Puerto Montt?", "Sí. Redactamos escrituras para Puerto Varas, Los Muermos, Calbuco, Maullín y alrededores, y coordinamos la firma de forma presencial u online."),
        ],
    },
    {
        "slug": "abogados-online-puerto-montt",
        "name": "Online",
        "title": "Abogados Online desde Puerto Montt",
        "card": "Abogados Online",
        "area": "Consulta online",
        "icon": "i-video",
        "sub": "Consulta por videollamada, todo Chile",
        "short": "Consultas y asesorías por videollamada para clientes de todo Chile, sin moverte de casa.",
        "lead": "Tu consulta legal por videollamada, con la misma dedicación que en persona. Atendemos a clientes de todo Chile.",
        "intro": "¿Vives fuera de Puerto Montt o no tienes tiempo de ir a la oficina? Agenda por WhatsApp o correo y conversamos por videollamada desde tu celular o computador. Los documentos se pueden enviar y revisar a distancia.",
        "items": [
            ("Agenda en minutos", "Por WhatsApp o correo electrónico."),
            ("Videollamada", "Desde tu celular o computador, sin instalar nada complicado."),
            ("Documentos a distancia", "Envío y revisión de antecedentes en línea."),
            ("Todas las materias", "Familia, penal, civil, laboral, herencias, empresas y más."),
        ],
        "callout": "La asesoría online es ideal para chilenos que viven en otra ciudad o en el extranjero y tienen asuntos legales en la Región de Los Lagos.",
        "faqs": [
            ("¿Qué necesito para la consulta online?", "Un celular o computador con internet y cámara. Te enviamos el enlace de la videollamada al agendar."),
            ("¿Puedo contratar el servicio completo a distancia?", "En muchos casos sí. Los documentos se pueden revisar en línea y, cuando se requiere firma ante notario, te indicamos cómo hacerlo."),
        ],
        "online": True,
    },
]
SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}

# SEO por servicio: título (<= 43 caracteres + " | Calixto & Cía."), meta descripción (<= 155),
# y encabezados H2 con palabras clave.
SEO = {
    "abogados-de-familia-puerto-montt": ("Abogados de Familia en Puerto Montt",
        "Abogados de familia en Puerto Montt: pensión de alimentos, divorcio, cuidado personal y VIF. Atención presencial u online. Agenda por WhatsApp.",
        "¿Por qué contar con un abogado de familia?", "Casos de familia que atendemos", "derecho de familia"),
    "abogados-de-divorcios-en-puerto-montt": ("Abogados de Divorcio en Puerto Montt",
        "Abogados de divorcio en Puerto Montt: mutuo acuerdo, unilateral y por culpa, compensación económica y liquidación de bienes. Agenda por WhatsApp.",
        "¿Por qué contar con un abogado de divorcio?", "Tipos de divorcio y trámites que atendemos", "divorcios"),
    "asesoria-bienes-raices-puerto-montt": ("Abogados Inmobiliarios en Puerto Montt",
        "Abogados inmobiliarios en Puerto Montt: estudio de títulos, compraventas, arriendos y subdivisiones de propiedades urbanas y rurales.",
        "¿Por qué asesorarte con un abogado inmobiliario?", "Servicios inmobiliarios que realizamos", "bienes raíces"),
    "abogados-penalistas-puerto-montt": ("Abogados Penalistas en Puerto Montt",
        "Abogados penalistas en Puerto Montt: control de detención, formalización, juicio oral y querellas. Defensa urgente al +56 9 9797 9827.",
        "¿Por qué contar con un abogado penalista?", "Casos penales que atendemos", "defensa penal"),
    "abogados-civiles-puerto-montt": ("Abogados Civiles en Puerto Montt",
        "Abogados civiles en Puerto Montt: juicios de tierras, precario, desalojos, arriendos, cobranzas e indemnizaciones. Agenda tu consulta por WhatsApp.",
        "¿Por qué contar con un abogado civil?", "Juicios civiles que atendemos", "juicios civiles"),
    "defensas-laborales": ("Abogados Laborales en Puerto Montt",
        "Abogados laborales en Puerto Montt: despido injustificado, nulidad del despido y accidentes del trabajo. Consulta antes de que venza el plazo.",
        "¿Por qué contar con un abogado laboral?", "Casos laborales que atendemos", "derecho laboral"),
    "posesion-efectiva-puerto-montt": ("Posesión Efectiva y Herencias Puerto Montt",
        "Tramitación de posesión efectiva y partición de herencias en Puerto Montt. Te ayudamos a regularizar los bienes heredados. Agenda por WhatsApp.",
        "¿Por qué tramitar tu herencia con un abogado?", "Trámites de herencia que realizamos", "posesión efectiva y herencias"),
    "abogados-policia-local-puerto-montt": ("Abogados Policía Local Puerto Montt",
        "Abogados de Policía Local en Puerto Montt: choques, accidentes de tránsito, infracciones y causas del consumidor. Cobra tus daños con nosotros.",
        "¿Por qué ir con abogado al Juzgado de Policía Local?", "Causas de Policía Local que atendemos", "Policía Local"),
    "sociedades-y-empresas-puerto-montt": ("Sociedades y Empresas en Puerto Montt",
        "Constitución de sociedades y Empresa en un Día en Puerto Montt. Asesoría legal para pymes y empresas, con apoyo contable. Agenda tu consulta.",
        "¿Por qué contar con un abogado para tu empresa?", "Servicios legales para empresas", "sociedades y empresas"),
    "redaccion-de-escrituras": ("Escrituras y Contratos en Puerto Montt",
        "Redacción de escrituras y contratos en Puerto Montt: compraventas, promesas, arriendos y poderes. También en Puerto Varas, Calbuco y Maullín.",
        "¿Por qué redactar tus contratos con un abogado?", "Escrituras y contratos que redactamos", "escrituras y contratos"),
    "abogados-online-puerto-montt": ("Abogados Online desde Puerto Montt",
        "Abogados online: consulta legal por videollamada con un estudio de Puerto Montt. Familia, penal, civil, laboral y más, para clientes de todo Chile.",
        "¿Cómo funciona la asesoría legal online?", "¿Qué incluye la asesoría online?", "asesoría online"),
}
SUFFIX = " | Calixto & Cía."

TEAM = [
    ("FC", "Fernando Calixto Marín", "Abogado · Director"),
    ("EZ", "E. Zapata", "Abogado(a) asociado(a)"),
    ("RC", "Roberto Calisto Villegas", "Contador auditor"),
]

# Artículos del blog. Se publican en las MISMAS URLs del WordPress actual para no perder
# posicionamiento. El texto es un borrador basado en la ley chilena: conviene reemplazarlo
# o revisarlo con el texto original de cada artículo antes de publicar.
POSTS = [
    {
        "path": "2025/11/08/la-accion-de-precario-en-chile/",
        "date": "2025-11-08", "date_txt": "8 de noviembre de 2025", "cat": "Artículos de Ayuda", "icon": "i-home",
        "title": "La Acción de Precario en Chile",
        "text": "Una herramienta del derecho civil para recuperar un inmueble ocupado por alguien sin contrato ni título que lo justifique.",
        "related": "abogados-civiles-puerto-montt",
        "body": """
          <p class="lead">La acción de precario es una institución de gran relevancia dentro del derecho civil chileno, destinada a proteger el derecho de dominio frente a la ocupación ilegítima de un bien. En la práctica, esta figura permite al propietario recuperar la tenencia de una cosa que se encuentra en manos de otra persona sin que exista título alguno que justifique dicha ocupación.</p>
          <h2>¿Qué es el precario?</h2>
          <p>El artículo 2195 inciso segundo del Código Civil señala que <em>“constituye también precario la tenencia de una cosa ajena, sin previo contrato y por ignorancia o mera tolerancia del dueño”</em>. Es decir, hay precario cuando una persona ocupa un bien que no le pertenece, sin un contrato u otro título que lo autorice, y solo porque el dueño no lo sabía o lo ha permitido por simple tolerancia.</p>
          <h2>Requisitos de la acción</h2>
          <p>Para que la demanda de precario prospere, los tribunales exigen acreditar tres elementos:</p>
          <ul>
            <li><strong>Que el demandante es dueño</strong> de la cosa, normalmente con la inscripción de dominio vigente en el Conservador de Bienes Raíces.</li>
            <li><strong>Que el demandado ocupa</strong> el bien.</li>
            <li><strong>Que esa ocupación no tiene título</strong>: no existe contrato ni otra razón jurídica que la justifique, y se debe a la ignorancia o mera tolerancia del dueño.</li>
          </ul>
          <p>Si el ocupante logra demostrar que tiene un título (por ejemplo, un contrato de arriendo o comodato vigente), la acción de precario no es la vía adecuada y deberán usarse otras acciones.</p>
          <h2>¿Cómo se tramita?</h2>
          <p>La acción de precario se tramita conforme al procedimiento sumario, ante el juzgado civil competente. Es un procedimiento más breve que el juicio ordinario, lo que la convierte en una herramienta eficaz para recuperar la propiedad.</p>
          <h2>Casos frecuentes</h2>
          <ul>
            <li>Familiares o conocidos a quienes se les permitió vivir “mientras tanto” y luego se niegan a salir.</li>
            <li>Ex parejas que permanecen en una vivienda que no les pertenece.</li>
            <li>Ocupación de terrenos o parcelas sin autorización del dueño.</li>
          </ul>
          <h2>¿Qué hacer si tienes este problema?</h2>
          <p>Reúne los antecedentes de tu dominio (inscripción en el Conservador, certificado de dominio vigente) y cualquier información sobre la ocupación. Con eso podemos evaluar si procede la acción de precario o si conviene otra vía, como la acción reivindicatoria o el término de un arriendo.</p>
""",
    },
    {
        "path": "2025/08/19/abogados-de-familia-en-puerto-montt-y-region-de-los-lagos/",
        "date": "2025-08-19", "date_txt": "19 de agosto de 2025", "cat": "Familia", "icon": "i-family",
        "title": "Abogados de Familia en Puerto Montt y Región de Los Lagos",
        "text": "Alimentos, divorcio, cuidado personal y medidas de protección: cómo te acompañamos ante los Tribunales de Familia.",
        "related": "abogados-de-familia-puerto-montt",
        "body": """
          <p class="lead">Los conflictos familiares son de los más sensibles que una persona puede enfrentar. Contar con un abogado de familia en Puerto Montt te permite conocer tus derechos, buscar acuerdos y, cuando es necesario, defender tus intereses y los de tus hijos ante el Tribunal de Familia.</p>
          <h2>Materias que atendemos</h2>
          <ul>
            <li><strong>Pensión de alimentos:</strong> demandas, aumentos, rebajas, cese y cobro de pensiones adeudadas.</li>
            <li><strong>Divorcio:</strong> de mutuo acuerdo, unilateral o por culpa, y la compensación económica asociada.</li>
            <li><strong>Cuidado personal</strong> de los hijos y <strong>relación directa y regular</strong> (régimen de visitas).</li>
            <li><strong>Violencia intrafamiliar</strong> y medidas de protección urgentes.</li>
          </ul>
          <h2>La mediación previa</h2>
          <p>En materias de alimentos, cuidado personal y relación directa y regular, la ley exige por regla general pasar por una mediación familiar antes de presentar la demanda. Es una oportunidad para llegar a un acuerdo; si no se logra, se obtiene el certificado que permite demandar. Te acompañamos también en esta etapa.</p>
          <h2>Divorcio: plazos de cese de convivencia</h2>
          <p>Para el divorcio de mutuo acuerdo se exige, por regla general, al menos un año de cese de la convivencia, y para el divorcio unilateral, al menos tres años. El divorcio por culpa no exige un plazo de separación, pero requiere acreditar una falta grave a los deberes del matrimonio.</p>
          <h2>Deudas de pensión de alimentos</h2>
          <p>Cuando no se pagan las pensiones, existen herramientas para su cobro, como la liquidación de la deuda, la retención de fondos y la inscripción del deudor en el Registro Nacional de Deudores de Pensiones de Alimentos, que trae consecuencias como restricciones para realizar ciertos trámites.</p>
          <h2>Atención en Puerto Montt y la Región de Los Lagos</h2>
          <p>Atendemos en nuestra oficina de Torre del Puerto, en el centro de Puerto Montt, y también por videollamada para clientes de Puerto Varas, Calbuco, Los Muermos, Maullín y el resto de la región.</p>
""",
    },
    {
        "path": "2025/02/10/corte-suprema-confirma-fallo-que-ordeno-a-beneficiada-restituir-vivienda-serviu/",
        "date": "2025-02-10", "date_txt": "10 de febrero de 2025", "cat": "Jurisprudencia", "icon": "i-news",
        "title": "Corte Suprema confirma fallo que ordenó a beneficiada restituir vivienda SERVIU",
        "seo_title": "Corte Suprema: restitución de vivienda SERVIU",
        "text": "El máximo tribunal declaró inadmisible la casación y dejó firme la acción reivindicatoria sobre la vivienda.",
        "related": "abogados-civiles-puerto-montt",
        "body": """
          <p class="lead">La Primera Sala de la Corte Suprema, de forma unánime, declaró inadmisible el recurso de casación interpuesto contra la sentencia que acogió una demanda reivindicatoria y ordenó restituir una vivienda asignada por SERVIU (causa rol N° 61.345-2024).</p>
          <h2>¿Qué decidió la Corte?</h2>
          <p>Al declarar inadmisible el recurso, la Corte Suprema no entró a revisar el fondo del asunto, por lo que quedó firme la sentencia que había ordenado la restitución del inmueble.</p>
          <h2>¿Qué es la acción reivindicatoria?</h2>
          <p>Según el artículo 889 del Código Civil, la reivindicación o acción de dominio es la que tiene el dueño de una cosa singular, de que no está en posesión, para que el poseedor sea condenado a restituírsela. Para que prospere se debe acreditar:</p>
          <ul>
            <li>Que el demandante es dueño de la cosa.</li>
            <li>Que el demandado está en posesión de ella.</li>
            <li>Que se trata de una cosa singular, debidamente individualizada.</li>
          </ul>
          <h2>¿Por qué es relevante?</h2>
          <p>El fallo confirma que las viviendas sociales también están protegidas por las acciones del derecho civil: quien la ocupa sin derecho puede ser obligado a restituirla a su dueño, aunque haya sido beneficiado anteriormente por un programa habitacional.</p>
          <h2>¿Tienes un caso similar?</h2>
          <p>Si alguien ocupa tu propiedad o te demandaron para restituir un inmueble, es importante revisar los títulos y la situación de posesión. Te ayudamos a definir si corresponde una acción reivindicatoria, de precario u otra vía.</p>
""",
    },
]

GENERAL_FAQS = [
    ("¿Cómo agendo una consulta?", f"Escríbenos por WhatsApp al {PHONE}, llámanos al {LANDLINE} o completa el formulario. Te contactaremos en horario hábil para coordinar día y hora."),
    ("¿Puedo tener la consulta por videollamada?", "Sí. Ofrecemos asesorías online por videoconferencia, ideal si vives fuera de Puerto Montt o no puedes trasladarte."),
    ("¿Dónde está la oficina?", "En Antonio Varas 216, Oficina 309, piso 3, Torre del Puerto, en el centro de Puerto Montt."),
    ("¿Qué debo llevar a la primera reunión?", "Tu cédula de identidad y cualquier documento relacionado con el caso: notificaciones, resoluciones, contratos, certificados o mensajes relevantes. Si no los tienes, igual podemos orientarte."),
    ("¿Atienden casos en Puerto Varas y otras comunas?", "Sí. Atendemos en Puerto Montt, Puerto Varas, Los Muermos, Calbuco, Maullín y el resto de la Provincia de Llanquihue, y a clientes de todo Chile de forma online."),
]

# ---------------------------------------------------------------------------
# Piezas comunes
# ---------------------------------------------------------------------------
EXTRA_ICONS = """    <symbol id="i-chat" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 9h8M8 13h5"/></g></symbol>
    <symbol id="i-rings" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="9" cy="14" r="6"/><circle cx="15" cy="10" r="6"/></g></symbol>
    <symbol id="i-key" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="7.5" cy="15.5" r="4.5"/><path d="m10.7 12.3 9.8-9.8M17 6l3 3M14.5 8.5l2 2"/></g></symbol>
    <symbol id="i-star" viewBox="0 0 24 24"><path fill="currentColor" d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/></symbol>
    <symbol id="i-chev" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="m6 9 6 6 6-6"/></symbol>
    <symbol id="i-info" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></g></symbol>
"""


def courthouse_svg():
    """Fachada neoclásica de tribunal en línea fina (decorativa)."""
    cols = []
    for cx in (95, 185, 275, 365, 455, 545):
        cols.append(
            f'<rect x="{cx-27}" y="150" width="54" height="10"/><rect x="{cx-22}" y="160" width="44" height="6"/>'
            f'<path d="M{cx-17} 166V356M{cx+17} 166V356M{cx-8.5} 170V352M{cx} 170V352M{cx+8.5} 170V352"/>'
            f'<rect x="{cx-23}" y="356" width="46" height="8"/><rect x="{cx-27}" y="364" width="54" height="6"/>')
    return ('<svg class="courthouse" viewBox="0 0 640 420" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true">'
            '<path class="draw" d="M30 122 320 18 610 122Z"/><path class="draw" d="M78 112 320 34 562 112Z"/>'
            '<path d="M302 88h36M320 70v30M306 76l-8 14h16zM334 76l-8 14h16z"/>'
            '<rect x="30" y="122" width="580" height="14"/><rect x="40" y="136" width="560" height="14"/>'
            + "".join(cols) +
            '<rect x="18" y="370" width="604" height="14"/><rect x="6" y="384" width="628" height="14"/><rect x="0" y="398" width="640" height="14"/>'
            '</svg>')


def scene(kind="page"):
    """Fondo del hero: degradado sobrio con la fachada de tribunal en dorado tenue."""
    return f"""      <div class="hero-bg" aria-hidden="true">
        <div class="hero-glow"></div>
        {courthouse_svg()}
        <div class="hero-vignette"></div>
      </div>
"""


def area_options(selected=None):
    opts = ['<option value="">Selecciona…</option>']
    for label in ["Familia", "Divorcio", "Penal", "Civil", "Bienes raíces", "Laboral", "Herencias / Posesión efectiva",
                  "Policía Local", "Sociedades y empresas", "Contratos y escrituras", "Consulta online", "Otra / No estoy seguro"]:
        sel = " selected" if label == selected else ""
        opts.append(f"<option{sel}>{escape(label)}</option>")
    return "".join(opts)


def quick_form(form_id, title, sub, selected=None, message=True):
    msg = f"""
            <div class="field">
              <label for="{form_id}-msg">Breve descripción <small>(opcional)</small></label>
              <textarea id="{form_id}-msg" name="mensaje" rows="3" placeholder="Cuéntanos brevemente tu caso"></textarea>
            </div>""" if message else ""
    return f"""<form class="card-form js-form" id="{form_id}" novalidate>
            <p class="form-title">{title}</p>
            <p class="sub">{sub}</p>
            <div class="field">
              <label for="{form_id}-nombre">Nombre</label>
              <input id="{form_id}-nombre" name="nombre" autocomplete="name" required placeholder="Tu nombre">
            </div>
            <div class="row-2">
              <div class="field">
                <label for="{form_id}-tel">Teléfono</label>
                <input id="{form_id}-tel" name="telefono" type="tel" autocomplete="tel" required placeholder="+56 9 ...">
              </div>
              <div class="field">
                <label for="{form_id}-area">Materia</label>
                <select id="{form_id}-area" name="area" required>{area_options(selected)}</select>
              </div>
            </div>{msg}
            <button type="submit" class="btn btn-wa btn-block"><svg><use href="#i-wa"/></svg> Enviar y agendar por WhatsApp</button>
            <p class="form-ok" hidden>¡Listo! Se abrió WhatsApp con tu mensaje. Solo presiona enviar.</p>
            <p class="form-note"><svg><use href="#i-lock"/></svg> Confidencial · protegido por el secreto profesional</p>
          </form>"""


def faq_block(faqs, open_first=True):
    out = []
    for i, (q, a) in enumerate(faqs):
        op = " open" if (i == 0 and open_first) else ""
        out.append(f"""          <details{op}>
            <summary><h3>{escape(q)}</h3></summary>
            <p>{escape(a)}</p>
          </details>""")
    return "\n".join(out)


def ld(obj):
    import json
    return f'\n  <script type="application/ld+json">{json.dumps(obj, ensure_ascii=False)}</script>'


def breadcrumb_ld(crumbs):
    """crumbs: lista de (nombre, ruta) desde la raíz."""
    return ld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + "/" + path} for i, (n, path) in enumerate(crumbs)]})


def faq_schema(faqs):
    import json
    return json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs],
    }, ensure_ascii=False)


def service_card(s, p, delay=0, detailed=False, num=None):
    if detailed:
        body = "<ul>" + "".join(f"<li>{escape(t)}</li>" for t, _ in s["items"][:5]) + "</ul>"
    else:
        body = f"<p>{escape(s['short'])}</p>"
    d = f' style="--d:{delay:.2f}s"' if delay else ""
    return f"""          <article class="service reveal"{d}>
            <div class="card-top"><div class="ic"><svg><use href="#{s['icon']}"/></svg></div>{f'<span class="num">{num:02d}</span>' if num else ''}</div>
            <h3>{escape(s['card'])}</h3>
            {body}
            <div class="actions">
              <a class="go" href="{p}portfolio-item/{s['slug']}/">Ver más<span class="sr-only"> sobre {escape(s['card'])}</span> <svg><use href="#i-arrow"/></svg></a>
              <a class="wa-mini js-wa" data-area="{escape(s['area'])}" data-track="tarjeta-servicio" href="#" aria-label="Consultar por WhatsApp sobre {escape(s['card'])}"><svg><use href="#i-wa"/></svg></a>
            </div>
          </article>"""


def services_grid(p, detailed=False):
    cards = [service_card(s, p, (i % 3) * 0.08, detailed, i + 1) for i, s in enumerate(SERVICES)]
    # Tarjeta de cierre: completa la grilla y ofrece contacto directo
    cards.append(f"""          <article class="service service-cta reveal">
            <h3>¿No encuentras tu materia?</h3>
            <p>Cuéntanos tu caso: te orientamos y, si no es nuestra área, te decimos a quién acudir.</p>
            <div class="actions"><a class="btn btn-wa js-wa" data-track="tarjeta-otra" href="#"><svg><use href="#i-wa"/></svg> Consultar por WhatsApp</a></div>
          </article>""")
    return "\n".join(cards)


def final_cta():
    return """    <section class="final-cta">
      <div class="hero-bg" aria-hidden="true"><div class="hero-glow"></div>""" + courthouse_svg() + """</div>
      <div class="container reveal zoom">
        <h2>¿Necesitas un abogado en Puerto Montt?</h2>
        <p>No dejes pasar los plazos legales. Escríbenos hoy y agenda tu consulta presencial u online.</p>
        <div class="hero-ctas">
          <a class="btn btn-wa js-wa" data-track="final" href="#"><svg><use href="#i-wa"/></svg> Escríbenos por WhatsApp</a>
          <a class="btn btn-light js-call" data-track="final" href="tel:""" + PHONE_TEL + """"><svg><use href="#i-phone"/></svg> Llamar ahora</a>
        </div>
      </div>
    </section>"""


TRIBUNALS = ["Corte Suprema", "Corte de Apelaciones de Puerto Montt", "Juzgados de Letras en lo Civil", "Juzgado de Familia",
             "Juzgado de Garantía", "Tribunal de Juicio Oral en lo Penal", "Juzgado de Letras del Trabajo", "Juzgados de Policía Local"]


def stats_band():
    items = [("+", YEARS, "", "Años de experiencia"), ("", RATING, "★", "Calificación en Google"),
             ("", REVIEWS, "", "Reseñas de clientes"), ("", str(len(SERVICES)), "", "Áreas de práctica")]
    cells = "\n".join(
        f'          <div class="stat reveal" style="--d:{i * .1:.1f}s"><span class="stat-n"><span class="count" data-to="{n}">{pre}{n}</span>{suf}</span><span class="stat-l">{l}</span></div>'
        for i, (pre, n, suf, l) in enumerate(items))
    return f"""    <section class="stats" aria-label="El estudio en cifras">
      <div class="container">
{cells}
      </div>
    </section>"""


def tribunals_band():
    names = "".join(f"<span>{escape(t)}</span>" for t in TRIBUNALS)
    return f"""    <section class="tribunals" aria-label="Tribunales">
      <p class="tribunals-title">Representamos a nuestros clientes ante</p>
      <div class="marquee"><div class="marquee-track">{names}{names}</div></div>
    </section>"""


def attorney_block(p, full=False):
    creds = [
        "Licenciado en Ciencias Jurídicas y Magíster en Derecho Privado (UACh).",
        "Diplomados en Derecho Procesal Avanzado y Litigación Oral (UC).",
        "Diplomados en Derecho Privado, Derecho Penal Sustantivo y Litigación Oral (USS).",
        "Miembro del Colegio de Abogados de Puerto Montt.",
    ]
    creds_html = "".join(f'<li><svg><use href="#i-check"/></svg> {escape(c)}</li>' for c in (creds if full else creds[:2] + creds[3:]))
    cta = "" if full else f'<a class="btn btn-navy" href="{p}quienes-somos/">Conoce al equipo <svg><use href="#i-arrow"/></svg></a>'
    return f"""    <section class="section attorney">
      <div class="container attorney-grid">
        <figure class="portrait reveal left">
          <!-- Reemplazar por la foto profesional del abogado: <img src="..." alt="Fernando Calixto Marín"> -->
          <div class="frame"><span class="mono">FC</span></div>
          <figcaption><strong>Fernando Calixto Marín</strong><span>Abogado · Director del estudio</span></figcaption>
        </figure>
        <div class="reveal right">
          <div class="eyebrow">{'Nuestro estudio' if full else 'El abogado'}</div>
          <h2>{'Experiencia, preparación y cercanía' if full else 'Fernando Calixto Marín'}</h2>
          <p class="lead">Con más de {YEARS} años de ejercicio, se ha dedicado a la asesoría legal y defensa judicial de personas, familias, negocios y empresas de Puerto Montt y la Región de Los Lagos.</p>
          <ul class="creds">{creds_html}</ul>
          <blockquote class="pull">Nuestro compromiso es que cada cliente entienda su situación, conozca sus alternativas y se sienta acompañado en todo el proceso.</blockquote>
          {cta}
        </div>
      </div>
    </section>"""


def values_block():
    vals = [("i-scale", "Ética profesional", "Actuamos con honestidad y te decimos con claridad qué se puede lograr y qué no."),
            ("i-lock", "Confidencialidad", "Tu caso está protegido por el secreto profesional desde la primera consulta."),
            ("i-shield", "Compromiso", "Defendemos tus intereses en todas las instancias, con seguimiento permanente."),
            ("i-chat", "Cercanía", "Trato directo con tu abogado y respuestas en lenguaje simple.")]
    cards = "\n".join(
        f'          <div class="value reveal" style="--d:{i * .1:.1f}s"><svg><use href="#{ic}"/></svg><h3>{t}</h3><p>{d}</p></div>'
        for i, (ic, t, d) in enumerate(vals))
    return f"""    <section class="section values-sec">
      <div class="container">
        <div class="section-head center reveal">
          <div class="eyebrow">Nuestros valores</div>
          <h2>Lo que nos define como estudio</h2>
        </div>
        <div class="values">
{cards}
        </div>
      </div>
    </section>"""


def reviews_block():
    return f"""    <section class="section reviews">
      <div class="container reviews-grid">
        <div class="reveal left">
          <div class="eyebrow">Opiniones de clientes</div>
          <h2>La confianza de quienes ya nos eligieron</h2>
          <p class="lead">Nuestros clientes nos califican con {RATING} estrellas en Google. Su recomendación es nuestro mejor respaldo.</p>
          <div class="hero-ctas" style="margin-bottom:0">
            <a class="btn btn-navy" href="{GOOGLE_REVIEWS}" target="_blank" rel="noopener">Ver reseñas en Google <svg><use href="#i-arrow"/></svg></a>
          </div>
        </div>
        <div class="rating-card reveal right">
          <span class="big">{RATING}</span>
          <span class="stars" aria-label="{RATING} de 5 estrellas">★★★★★</span>
          <span class="count-line"><strong>{REVIEWS}</strong> reseñas en Google</span>
          <span class="seal">Clientes de Puerto Montt y la Región de Los Lagos</span>
        </div>
      </div>
    </section>"""


def quote_band():
    return f"""    <section class="quote-band">
      <div class="hero-bg" aria-hidden="true"><div class="hero-glow"></div>{courthouse_svg()}</div>
      <div class="container reveal zoom">
        <blockquote>«La justicia es la constante y perpetua voluntad de dar a cada uno su derecho.»</blockquote>
        <cite>Ulpiano · Digesto</cite>
      </div>
    </section>"""


def post_cards(p):
    return "\n".join(f"""          <a class="post reveal" style="--d:{i * 0.1:.1f}s" href="{p}{x['path']}">
            <div class="cover"><span class="cat">{escape(x['cat'])}</span><svg><use href="#{x['icon']}"/></svg></div>
            <div class="body">
              <time datetime="{x['date']}">{x['date_txt']}</time>
              <h3>{escape(x['title'])}</h3>
              <p>{escape(x['text'])}</p>
              <span class="read">Leer artículo <svg width="16" height="16"><use href="#i-arrow"/></svg></span>
            </div>
          </a>""" for i, x in enumerate(POSTS))


def page_hero(p, crumbs, title, lead, area=None, extra=""):
    items = [f'<li><a href="{p}">Inicio</a></li>']
    for label, href in crumbs:
        items.append(f'<li><a href="{href}">{escape(label)}</a></li>' if href else f'<li aria-current="page">{escape(label)}</li>')
    data_area = f' data-area="{escape(area)}"' if area else ""
    return f"""    <section class="page-hero">
{scene("page")}
      <div class="container hero-in">
        <ol class="crumbs">{''.join(items)}</ol>
        <h1>{title}</h1>
        <p class="lead">{lead}</p>
        <div class="hero-ctas">
          <a class="btn btn-wa js-wa"{data_area} data-track="page-hero" href="#"><svg><use href="#i-wa"/></svg> Agendar por WhatsApp</a>
          <a class="btn btn-ghost js-call" data-track="page-hero" href="tel:{PHONE_TEL}"><svg><use href="#i-phone"/></svg> {PHONE}</a>
        </div>{extra}
      </div>
    </section>"""


def layout(path, title, description, active, body, p, extra_head="", noindex=False):
    sprite = open(os.path.join(ROOT, "build", "sprite.html")).read()
    sprite = sprite.replace("  </svg>\n", EXTRA_ICONS + "  </svg>\n", 1)
    canonical = SITE + "/" + path

    def nav_link(key, href, label):
        cls = "link active" if active == key else "link"
        cur = ' aria-current="page"' if active == key else ""
        return f'<a class="{cls}" href="{href}"{cur}>{label}</a>'

    def sub_link(s):
        cls = ' class="active"' if active == s["slug"] else ""
        return (f'          <a href="{p}portfolio-item/{s["slug"]}/"{cls}><span class="ic"><svg><use href="#{s["icon"]}"/></svg></span>'
                f'<span><strong>{escape(s["card"])}</strong><small>{escape(s["sub"])}</small></span></a>')
    sub = "\n".join(sub_link(s) for s in SERVICES)
    serv_active = active == "servicios" or active in SERVICE_BY_SLUG
    sites = "\n".join(f'            <li><a href="https://www.{d}" target="_blank" rel="noopener">{d}</a></li>' for d in SISTER_SITES)
    footer_services = "\n".join(
        f'            <li><a href="{p}portfolio-item/{s["slug"]}/">{escape(s["card"])}</a></li>' for s in SERVICES)

    return f"""<!doctype html>
<html lang="es-CL">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}">
  {'<meta name="robots" content="noindex, follow">' if noindex else f'<link rel="canonical" href="{canonical}">'}
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Abogados en Puerto Montt · Estudio Calixto &amp; Cía.">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE}/assets/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta property="og:locale" content="es_CL">
  <meta name="theme-color" content="#1b3263">
  <link rel="icon" href="{p}assets/logo.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Playfair+Display:ital,wght@0,600;0,700;1,600&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{p}assets/css/styles.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LegalService",
    "name": "Abogados en Puerto Montt - Estudio Calixto & Cía.",
    "url": "{SITE}/",
    "logo": "{SITE}/assets/logo.png",
    "telephone": "{PHONE_TEL}",
    "email": "{EMAIL}",
    "address": {{"@type": "PostalAddress", "streetAddress": "Antonio Varas 216, Oficina 309, Piso 3, Torre del Puerto", "addressLocality": "Puerto Montt", "addressRegion": "Los Lagos", "addressCountry": "CL"}},
    "areaServed": ["Puerto Montt", "Puerto Varas", "Los Muermos", "Calbuco", "Maullín", "Provincia de Llanquihue", "Chile"],
    "openingHoursSpecification": [
      {{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "09:00", "closes": "13:00"}},
      {{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "15:00", "closes": "18:30"}}
    ],
    "founder": {{"@type": "Person", "name": "Fernando Calixto Marín", "jobTitle": "Abogado"}},
    "sameAs": ["{FACEBOOK}"]
  }}
  </script>{extra_head}
</head>
<body>
  <div class="progress" aria-hidden="true"></div>
{sprite}
  <!-- Franja de urgencia penal -->
  <div class="alert-bar" id="alert-bar" role="region" aria-label="Defensa penal urgente">
    <div class="container">
      <span class="siren" aria-hidden="true"></span>
      <span><strong>¿Detenido o formalizado?</strong> <span class="hide-xs">Defensa penal urgente:</span></span>
      <a class="js-call" data-track="urgencia-penal" href="tel:{PHONE_TEL}">Llama al {PHONE}</a>
      <button class="close" type="button" aria-label="Cerrar aviso">&times;</button>
    </div>
  </div>

  <!-- Barra superior -->
  <div class="topbar">
    <div class="container">
      <span class="hide-sm"><svg><use href="#i-pin"/></svg> Antonio Varas 216, Of. 309, Torre del Puerto</span>
      <div class="ticker" aria-live="polite">
        <span class="on" id="tk-status"><i class="live-dot"></i> Abierto ahora · <b>Respondemos por WhatsApp</b></span>
        <a class="js-wa" data-track="topbar-ticker" href="#"><svg><use href="#i-cal"/></svg> Agenda tu consulta · <b>presencial u online</b></a>
        <span><svg><use href="#i-video"/></svg> Atención online para clientes de <b>todo Chile</b></span>
        <span><svg><use href="#i-clock"/></svg> Lun a Vie · <b>09:00–13:00 y 15:00–18:30</b></span>
      </div>
      <div class="tb-right hide-sm">
        <a class="js-call" data-track="topbar" href="tel:{LANDLINE_TEL}"><svg><use href="#i-phone"/></svg> {LANDLINE}</a>
        <a class="tb-social" href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Facebook"><svg><use href="#i-fb"/></svg></a>
      </div>
    </div>
  </div>

  <!-- Header -->
  <header class="header">
    <div class="container">
      <a href="{p}" class="brand" aria-label="Inicio">
        <img src="{p}assets/logo.png" alt="Calixto &amp; Cía. Abogados | Estudio Jurídico" width="192" height="52">
      </a>
      <button class="menu-toggle" aria-label="Abrir menú" aria-expanded="false" aria-controls="nav"><svg><use href="#i-menu"/></svg></button>
      <nav class="nav" id="nav">
        {nav_link('inicio', p or './', 'Inicio')}
        <div class="nav-item has-sub">
          <a class="{'link active' if serv_active else 'link'}" href="{p}servicios/">Servicios</a>
          <button class="sub-toggle" type="button" aria-expanded="false" aria-label="Ver servicios"><svg><use href="#i-chev"/></svg></button>
          <div class="submenu">
{sub}
          <a class="all" href="{p}servicios/">Ver todos los servicios →</a>
          </div>
        </div>
        {nav_link('nosotros', p + 'quienes-somos/', 'Quiénes somos')}
        {nav_link('blog', p + 'blog/', 'Blog')}
        {nav_link('contacto', p + 'contacto/', 'Contacto')}
        <a class="nav-phone js-call" data-track="header" href="tel:{PHONE_TEL}"><svg><use href="#i-phone"/></svg> {PHONE}</a>
        <a class="btn btn-wa js-wa" data-track="header" href="#"><svg><use href="#i-wa"/></svg> Agendar consulta</a>
      </nav>
    </div>
  </header>

  <main>
{body}
  </main>

  <footer>
    <div class="container">
      <div class="foot">
        <div>
          <div class="brand-footer"><img src="{p}assets/logo-white.png" alt="Calixto &amp; Cía. Abogados" width="207" height="56"></div>
          <p>Estudio jurídico multidisciplinario. Asesoría y defensa judicial en Puerto Montt, Puerto Varas y la Provincia de Llanquihue.</p>
          <p><a href="{p}quienes-somos/">Quiénes somos</a> · <a href="{p}blog/">Blog</a> · <a href="{p}contacto/">Contacto</a></p>
        </div>
        <div>
          <p class="foot-title">Servicios</p>
          <ul>
{footer_services}
          </ul>
        </div>
        <div>
          <p class="foot-title">Contacto</p>
          <ul>
            <li><a class="js-wa" data-track="footer" href="#">{PHONE}</a></li>
            <li><a class="js-call" data-track="footer" href="tel:{LANDLINE_TEL}">{LANDLINE}</a></li>
            <li><a class="js-mail" data-track="footer" href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li>Antonio Varas 216, Of. 309, Puerto Montt</li>
            <li>Lun a Vie · 09:00–13:00 y 15:00–18:30</li>
            <li><a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a></li>
          </ul>
          <p class="foot-title" style="margin-top:1.4rem">Nuestros sitios</p>
          <ul class="sites">
{sites}
          </ul>
        </div>
      </div>
      <div class="copy">
        <span>© <span class="js-year">2026</span> Abogados en Puerto Montt · Estudio Calixto &amp; Cía.</span>
        <span>Puerto Montt, Región de Los Lagos, Chile</span>
      </div>
    </div>
  </footer>

  <!-- Flotantes -->
  <button class="to-top" aria-label="Volver arriba"><svg><use href="#i-arrow"/></svg></button>
  <a class="wa-float js-wa" data-track="flotante" href="#" aria-label="Escríbenos por WhatsApp">
    <svg><use href="#i-wa"/></svg>
    <span class="tip">¿Hablamos? Agenda tu consulta</span>
  </a>
  <div class="mobile-bar">
    <a class="btn btn-navy js-call" data-track="barra-movil" href="tel:{PHONE_TEL}"><svg><use href="#i-phone"/></svg> Llamar</a>
    <a class="btn btn-wa js-wa" data-track="barra-movil" href="#"><svg><use href="#i-wa"/></svg> WhatsApp</a>
  </div>

  <script src="{p}assets/js/main.js" defer></script>
</body>
</html>
"""


def write(path, html):
    full = os.path.join(ROOT, path, "index.html") if path and not path.endswith(".html") else os.path.join(ROOT, path or "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    return full


def rel(path):
    depth = path.strip("/").count("/") + 1 if path.strip("/") else 0
    return "../" * depth


# ---------------------------------------------------------------------------
# Páginas
# ---------------------------------------------------------------------------
def build_home():
    p = ""
    body = f"""    <section class="hero">
{scene("home")}
      <div class="container">
        <div class="hero-in">
          <div class="eyebrow">Estudio Jurídico Calixto &amp; Cía.</div>
          <h1>Abogados en Puerto Montt</h1>
          <p class="hero-sub">Defensa legal seria, cercana y confidencial.</p>
          <p class="lead">Asesoría y representación judicial en familia, penal, civil, laboral, herencias y empresas. Atención presencial en Torre del Puerto y online para todo Chile.</p>
          <div class="hero-ctas">
            <a class="btn btn-wa js-wa" data-track="hero" href="#"><svg><use href="#i-wa"/></svg> Agendar por WhatsApp</a>
            <a class="btn btn-ghost js-call" data-track="hero" href="tel:{PHONE_TEL}"><svg><use href="#i-phone"/></svg> {PHONE}</a>
          </div>
          <ul class="trust">
            <li><a class="rating" href="{GOOGLE_REVIEWS}" target="_blank" rel="noopener"><span class="stars" aria-hidden="true">★★★★★</span> <b>{RATING}</b> en Google · {REVIEWS} reseñas</a></li>
            <li><svg><use href="#i-award"/></svg> Colegio de Abogados de Puerto Montt</li>
          </ul>
        </div>

        <div class="form-wrap">
          {quick_form("form-hero", "Solicite su consulta", "Déjenos sus datos y lo contactamos en horario hábil.", message=False)}
        </div>
      </div>
    </section>

{stats_band()}

    <section class="section" id="servicios">
      <div class="container">
        <div class="section-head split reveal">
          <div>
            <div class="eyebrow">Áreas de práctica</div>
            <h2>Asesoría y defensa en las materias que más importan</h2>
          </div>
          <p class="lead">Representamos a personas, familias y empresas en todas las etapas del proceso, desde la primera consulta hasta la sentencia.</p>
        </div>
        <div class="services cols-3 compact">
{services_grid(p)}
        </div>
      </div>
    </section>

{attorney_block(p)}

{tribunals_band()}

{values_block()}

    <section class="section process" id="como-trabajamos">
      <div class="container">
        <div class="section-head center reveal">
          <div class="eyebrow">Cómo trabajamos</div>
          <h2>Tres pasos para comenzar</h2>
        </div>
        <div class="steps">
          <div class="step reveal"><div class="n">I</div><h3>Primera consulta</h3><p>Escríbanos por WhatsApp, teléfono o formulario con un breve resumen de su situación.</p></div>
          <div class="step reveal" style="--d:.15s"><div class="n">II</div><h3>Análisis del caso</h3><p>Nos reunimos en Torre del Puerto o por videollamada y revisamos sus antecedentes.</p></div>
          <div class="step reveal" style="--d:.3s"><div class="n">III</div><h3>Estrategia y acción</h3><p>Le explicamos alternativas, plazos y honorarios, con facilidades de pago, y comenzamos a trabajar.</p></div>
        </div>
      </div>
    </section>

{reviews_block()}

{quote_band()}

    <section class="section">
      <div class="container">
        <div class="section-head split reveal">
          <div>
            <div class="eyebrow">Actualidad legal</div>
            <h2>Publicaciones recientes</h2>
          </div>
          <p><a class="btn btn-outline" href="{p}blog/">Ver todas las publicaciones <svg><use href="#i-arrow"/></svg></a></p>
        </div>
        <div class="posts">
{post_cards(p)}
        </div>
      </div>
    </section>

{final_cta()}"""
    return layout("", "Abogados en Puerto Montt | Estudio Calixto & Cía.",
                  "Abogados en Puerto Montt: familia, penal, civil, laboral, herencias y empresas. Atención presencial u online. Agenda tu consulta por WhatsApp.",
                  "inicio", body, p)


SCALES = """<svg class="scales" viewBox="0 0 200 200" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M100 40v130M65 175h70"/><circle cx="100" cy="40" r="7"/>
            <g class="beam">
              <path d="M40 52h120"/>
              <path d="M40 52 20 105a22 22 0 0 0 40 0L40 52zM160 52l-20 53a22 22 0 0 0 40 0l-20-53z"/>
            </g>
          </svg>"""


def build_services():
    path = "servicios/"
    p = rel(path)
    body = f"""{page_hero(p, [("Servicios", None)], "Servicios legales en Puerto Montt", "Asesoría y representación judicial para personas, familias y empresas, desde la primera consulta hasta la sentencia.")}

    <section class="section">
      <div class="container">
        <div class="section-head center reveal">
          <div class="eyebrow">Áreas de práctica</div>
          <h2>Nuestras áreas de práctica en Puerto Montt</h2>
        </div>
        <div class="services cols-3">
{services_grid(p, detailed=True)}
        </div>
      </div>
    </section>

    <section class="section process">
      <div class="container">
        <div class="section-head center reveal">
          <div class="eyebrow">Preguntas frecuentes</div>
          <h2>Resolvemos tus dudas</h2>
        </div>
        <div class="faq reveal">
{faq_block(GENERAL_FAQS)}
        </div>
      </div>
    </section>

{final_cta()}"""
    return path, layout(path, "Servicios Legales en Puerto Montt" + SUFFIX,
                        "Abogados de familia, penal, civil, laboral, herencias, Policía Local, sociedades, contratos y asesoría online en Puerto Montt.",
                        "servicios", body, p, f'\n  <script type="application/ld+json">{faq_schema(GENERAL_FAQS)}</script>'
                        + breadcrumb_ld([("Inicio", ""), ("Servicios", path)]))


CALL_MOCK = """<div class="call-mock reveal" aria-hidden="true" style="margin:1.6rem 0">
            <div class="call-bar"><i></i><i></i><i></i><span>Consulta legal · Calixto &amp; Cía.</span><span class="live">En vivo</span></div>
            <div class="call-grid">
              <div class="tile big"><div class="avatar">FC</div><span class="name">Abogado</span><div class="wave"><b></b><b></b><b></b><b></b></div></div>
              <div class="tile s1"><div class="avatar">Tú</div><span class="name">Cliente</span></div>
              <div class="tile s2"><svg width="40" height="40" style="color:#a9e7c0"><use href="#i-doc"/></svg><span class="name">Documentos</span></div>
            </div>
            <div class="call-ctrl"><span><svg><use href="#i-mic"/></svg></span><span><svg><use href="#i-video"/></svg></span><span class="end"><svg><use href="#i-phone"/></svg></span></div>
          </div>"""


def build_service(s):
    path = f"portfolio-item/{s['slug']}/"
    p = rel(path)
    seo_title, seo_desc, seo_why, seo_items, seo_topic = SEO[s["slug"]]
    items = "\n".join(
        f'            <li><svg><use href="#i-check"/></svg><div><h3>{escape(t)}</h3><span>{escape(d)}</span></div></li>'
        for t, d in s["items"])
    idx = SERVICES.index(s)
    others = [SERVICES[(idx + k) % len(SERVICES)] for k in (1, 2, 3)]
    related = "\n".join(
        f'          <a class="rel reveal" href="{p}portfolio-item/{o["slug"]}/"><span class="ic"><svg><use href="#{o["icon"]}"/></svg></span><span><strong>{escape(o["card"])}</strong><span>{escape(o["sub"])}</span></span></a>'
        for o in others)
    online_extra = CALL_MOCK if s.get("online") else ""
    body = f"""{page_hero(p, [("Servicios", p + "servicios/"), (s["card"], None)], escape(s["title"]), escape(s["lead"]), area=s["area"])}

    <section class="section">
      <div class="container detail">
        <article class="prose">
          <h2 class="reveal">{escape(seo_why)}</h2>
          <p class="reveal">{escape(s["intro"])}</p>
          {online_extra}
          <h2 class="reveal">{escape(seo_items)}</h2>
          <ul class="checklist reveal">
{items}
          </ul>
          <div class="callout reveal"><svg><use href="#i-info"/></svg><p>{escape(s["callout"])}</p></div>
          <h2 class="reveal">¿Cómo trabajamos tu caso?</h2>
          <ol class="mini-steps reveal">
            <li><div><strong>Primera consulta.</strong> Escuchamos tu caso y revisamos tus documentos, presencial u online.</div></li>
            <li><div><strong>Estrategia clara.</strong> Te explicamos alternativas, plazos y costos antes de empezar.</div></li>
            <li><div><strong>Acción y seguimiento.</strong> Tramitamos tu caso y te informamos de cada avance.</div></li>
          </ol>
          <h2 class="reveal">Preguntas frecuentes sobre {escape(seo_topic)}</h2>
          <div class="faq reveal" style="margin:0">
{faq_block(s["faqs"])}
          </div>
        </article>

        <aside class="sidebar">
          {quick_form("form-servicio", "Consulta tu caso", "Te respondemos por WhatsApp para agendar.", selected=s["area"])}
          <div class="call-box">
            <strong>¿Prefieres llamar?</strong>
            <p>{HOURS}<span class="open-now" hidden></span></p>
            <a class="btn btn-light js-call" data-track="sidebar" href="tel:{PHONE_TEL}"><svg><use href="#i-phone"/></svg> {PHONE}</a>
          </div>
        </aside>
      </div>
    </section>

    <section class="section process" style="padding-block:64px">
      <div class="container">
        <div class="section-head reveal" style="margin-bottom:28px">
          <div class="eyebrow">Otros servicios</div>
          <h2 style="font-size:1.6rem">También te podemos ayudar con</h2>
        </div>
        <div class="related">
{related}
        </div>
      </div>
    </section>

{final_cta()}"""
    service_ld = ld({
        "@context": "https://schema.org", "@type": "Service", "name": s["title"], "serviceType": s["card"],
        "description": seo_desc, "url": SITE + "/" + path, "areaServed": {"@type": "City", "name": "Puerto Montt"},
        "provider": {"@type": "LegalService", "name": "Abogados en Puerto Montt - Estudio Calixto & Cía.", "url": SITE + "/", "telephone": PHONE_TEL},
    })
    return path, layout(path, seo_title + SUFFIX, seo_desc, s["slug"], body, p,
                        f'\n  <script type="application/ld+json">{faq_schema(s["faqs"])}</script>' + service_ld
                        + breadcrumb_ld([("Inicio", ""), ("Servicios", "servicios/"), (s["card"], path)]))


def build_about():
    path = "quienes-somos/"
    p = rel(path)
    team = "\n".join(
        f'          <div class="member reveal" style="--d:{i * 0.1:.1f}s"><div class="av">{a}</div><div><strong>{escape(n)}</strong><span>{escape(r)}</span></div></div>'
        for i, (a, n, r) in enumerate(TEAM))
    body = f"""{page_hero(p, [("Quiénes somos", None)], "Quiénes somos", "Un equipo de abogados especializados en distintas áreas del derecho, al servicio de Puerto Montt y la Región de Los Lagos.")}

{attorney_block(p, full=True)}

    <section class="section" style="padding-top:0">
      <div class="container">
        <div class="section-head reveal">
          <div class="eyebrow">Equipo</div>
          <h2>Profesionales que lo acompañan</h2>
          <p class="lead">Mantenemos honorarios razonables y otorgamos facilidades de pago, aprovechando la tramitación electrónica para reducir costos sin bajar la calidad.</p>
        </div>
        <!-- Equipo (confirmar nombres y cargos con el estudio) -->
        <div class="team">
{team}
        </div>
      </div>
    </section>

{values_block()}

{reviews_block()}

    <section class="section" style="padding-block:72px">
      <div class="container">
        <div class="section-head center reveal" style="margin-bottom:0">
          <div class="eyebrow">Cobertura</div>
          <h2>Atendemos en toda la Provincia de Llanquihue</h2>
          <p class="lead">Representamos causas en los tribunales de estas comunas. Si vives en otra parte de Chile, te atendemos por videollamada.</p>
          <ul class="areas">
            <li class="main"><svg><use href="#i-pin"/></svg> Puerto Montt <small>Oficina</small></li>
            <li><svg><use href="#i-pin"/></svg> Puerto Varas</li><li><svg><use href="#i-pin"/></svg> Llanquihue</li><li><svg><use href="#i-pin"/></svg> Frutillar</li>
            <li><svg><use href="#i-pin"/></svg> Los Muermos</li><li><svg><use href="#i-pin"/></svg> Calbuco</li><li><svg><use href="#i-pin"/></svg> Maullín</li><li><svg><use href="#i-pin"/></svg> Fresia</li>
          </ul>
          <p style="margin-top:1.4rem"><a class="btn btn-navy" href="{p}portfolio-item/abogados-online-puerto-montt/"><svg><use href="#i-video"/></svg> ¿Estás en otra ciudad? Consulta online</a></p>
        </div>
      </div>
    </section>

{final_cta()}"""
    return path, layout(path, "Quiénes Somos | Abogados en Puerto Montt" + SUFFIX,
                        "Conoce al Estudio Calixto & Cía.: abogados en Puerto Montt liderados por Fernando Calixto Marín, Magíster en Derecho Privado (UACh).",
                        "nosotros", body, p, breadcrumb_ld([("Inicio", ""), ("Quiénes somos", path)]))


def build_blog():
    path = "blog/"
    p = rel(path)
    posts = post_cards(p)
    body = f"""{page_hero(p, [("Blog", None)], "Blog jurídico", "Información clara sobre tus derechos y fallos relevantes de los tribunales chilenos.")}

    <section class="section">
      <div class="container">
        <div class="section-head reveal">
          <div class="eyebrow">Publicaciones</div>
          <h2>Últimos artículos</h2>
        </div>
        <div class="posts">
{posts}
        </div>
      </div>
    </section>

{final_cta()}"""
    return path, layout(path, "Blog Jurídico | Abogados en Puerto Montt" + SUFFIX,
                        "Artículos y noticias legales del Estudio Calixto & Cía. de Puerto Montt: derecho civil, familia, acción de precario y fallos de la Corte Suprema.",
                        "blog", body, p, breadcrumb_ld([("Inicio", ""), ("Blog", path)]))


def build_post(x):
    path = x["path"]
    p = rel(path)
    svc = SERVICE_BY_SLUG[x["related"]]
    others = "\n".join(
        f'            <li><a href="{p}{o["path"]}"><time datetime="{o["date"]}">{o["date_txt"]}</time>{escape(o["title"])}</a></li>'
        for o in POSTS if o is not x)
    body = f"""{page_hero(p, [("Blog", p + "blog/"), (x["title"], None)], escape(x["title"]), f'<time datetime="{x["date"]}">{x["date_txt"]}</time> · {escape(x["cat"])} · Estudio Calixto &amp; Cía.', area=svc["area"])}

    <section class="section">
      <div class="container detail">
        <article class="prose article">
          <div class="post-cover reveal"><svg><use href="#{x['icon']}"/></svg><span class="cat">{escape(x['cat'])}</span></div>
{x["body"]}
          <div class="callout reveal"><svg><use href="#i-info"/></svg><p>Este artículo es informativo y no reemplaza una asesoría legal. Cada caso es distinto: escríbenos y revisamos el tuyo.</p></div>
          <p><a class="btn btn-navy" href="{p}portfolio-item/{svc['slug']}/">Ver servicio de {escape(svc['card'])} <svg><use href="#i-arrow"/></svg></a></p>
        </article>

        <aside class="sidebar">
          {quick_form("form-articulo", "¿Tienes un caso similar?", "Cuéntanos y te respondemos por WhatsApp.", selected=svc["area"], message=False)}
          <div class="side-list">
            <p class="form-title">Otras publicaciones</p>
            <ul>
{others}
            </ul>
            <a class="go" href="{p}blog/">Ver todo el blog →</a>
          </div>
        </aside>
      </div>
    </section>

{final_cta()}"""
    article_ld = ld({
        "@context": "https://schema.org", "@type": "BlogPosting", "headline": x["title"], "datePublished": x["date"],
        "description": x["text"], "url": SITE + "/" + path, "image": SITE + "/assets/og-image.png",
        "author": {"@type": "Organization", "name": "Estudio Calixto & Cía."},
        "publisher": {"@type": "Organization", "name": "Estudio Calixto & Cía.", "logo": {"@type": "ImageObject", "url": SITE + "/assets/logo.png"}},
    })
    title = x.get("seo_title", x["title"])
    if len(title + SUFFIX) <= 62:
        title += SUFFIX
    return path, layout(path, title, x["text"], "blog", body, p,
                        article_ld + breadcrumb_ld([("Inicio", ""), ("Blog", "blog/"), (x["title"], path)]))


def build_contact():
    path = "contacto/"
    p = rel(path)
    body = f"""{page_hero(p, [("Contacto", None)], "Contacto", "Escríbenos y te responderemos a la brevedad para agendar tu consulta presencial u online.")}

    <section class="section">
      <div class="container contact">
        <div class="reveal left">
          <div class="eyebrow">Datos de contacto</div>
          <h2>Hablemos de tu caso</h2>
          <ul class="contact-list">
            <li><div class="ic"><svg><use href="#i-wa"/></svg></div><div><strong>WhatsApp / Celular</strong><a class="js-wa" data-track="contacto" href="#">{PHONE}</a></div></li>
            <li><div class="ic"><svg><use href="#i-phone"/></svg></div><div><strong>Teléfono fijo</strong><a class="js-call" data-track="contacto" href="tel:{LANDLINE_TEL}">{LANDLINE}</a></div></li>
            <li><div class="ic"><svg><use href="#i-mail"/></svg></div><div><strong>Correo</strong><a class="js-mail" data-track="contacto" href="mailto:{EMAIL}">{EMAIL}</a></div></li>
            <li><div class="ic"><svg><use href="#i-pin"/></svg></div><div><strong>Oficina</strong><span>{ADDRESS}</span></div></li>
            <li><div class="ic"><svg><use href="#i-clock"/></svg></div><div><strong>Horario <span class="open-now" hidden></span></strong><span>{HOURS}</span></div></li>
          </ul>
          <div class="map">
            <iframe title="Mapa: Torre del Puerto, Antonio Varas 216, Puerto Montt" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
              src="https://maps.google.com/maps?q=Antonio%20Varas%20216%2C%20Puerto%20Montt%2C%20Chile&amp;z=16&amp;output=embed"></iframe>
          </div>
        </div>

        <form class="card-form js-form reveal right" id="form-contacto" novalidate>
          <p class="form-title">Solicita tu consulta</p>
          <p class="sub">Completa tus datos y elige cómo prefieres enviarlos.</p>
          <div class="field">
            <label for="c-nombre">Nombre completo</label>
            <input id="c-nombre" name="nombre" autocomplete="name" required placeholder="Tu nombre">
          </div>
          <div class="row-2">
            <div class="field">
              <label for="c-tel">Teléfono</label>
              <input id="c-tel" name="telefono" type="tel" autocomplete="tel" required placeholder="+56 9 ...">
            </div>
            <div class="field">
              <label for="c-email">Correo (opcional)</label>
              <input id="c-email" name="email" type="email" autocomplete="email" placeholder="tu@correo.cl">
            </div>
          </div>
          <div class="row-2">
            <div class="field">
              <label for="c-area">Materia</label>
              <select id="c-area" name="area" required>{area_options()}</select>
            </div>
            <div class="field">
              <label for="c-modo">Modalidad</label>
              <select id="c-modo" name="modalidad">
                <option>Presencial</option>
                <option>Online (videollamada)</option>
                <option>Me da igual</option>
              </select>
            </div>
          </div>
          <div class="field">
            <label for="c-msg">Cuéntanos tu caso</label>
            <textarea id="c-msg" name="mensaje" rows="4" placeholder="Describe brevemente tu situación"></textarea>
          </div>
          <button type="submit" class="btn btn-wa btn-block"><svg><use href="#i-wa"/></svg> Enviar por WhatsApp</button>
          <a href="#" class="form-alt js-form-mail" data-form="form-contacto">Prefiero enviarlo por correo</a>
          <p class="form-ok" hidden>¡Listo! Se abrió WhatsApp con tu mensaje. Solo presiona enviar.</p>
          <p class="form-note"><svg><use href="#i-lock"/></svg> Confidencial · protegido por el secreto profesional</p>
        </form>
      </div>
    </section>

    <section class="section process">
      <div class="container">
        <div class="section-head center reveal">
          <div class="eyebrow">Preguntas frecuentes</div>
          <h2>Antes de tu consulta</h2>
        </div>
        <div class="faq reveal">
{faq_block(GENERAL_FAQS)}
        </div>
      </div>
    </section>"""
    return path, layout(path, "Contacto | Abogados en Puerto Montt" + SUFFIX,
                        f"Contacta al Estudio Calixto & Cía. en Torre del Puerto, Puerto Montt. WhatsApp {PHONE}, teléfono {LANDLINE}, {EMAIL}.",
                        "contacto", body, p, f'\n  <script type="application/ld+json">{faq_schema(GENERAL_FAQS)}</script>'
                        + breadcrumb_ld([("Inicio", ""), ("Contacto", path)]))


def build_404():
    p = "/"
    body = f"""{page_hero(p, [("Página no encontrada", None)], "Página no encontrada", "La página que buscas no existe o cambió de dirección. Revisa nuestros servicios o escríbenos directamente.")}

    <section class="section">
      <div class="container notfound">
        <div class="big">404</div>
        <p class="lead">¿Buscabas algún servicio en particular?</p>
        <div class="hero-ctas" style="justify-content:center">
          <a class="btn btn-navy" href="/servicios/">Ver servicios</a>
          <a class="btn btn-wa js-wa" data-track="404" href="#"><svg><use href="#i-wa"/></svg> Escríbenos</a>
        </div>
      </div>
    </section>"""
    # Rutas absolutas: el 404 puede mostrarse en cualquier URL.
    return layout("404.html", "Página no encontrada" + SUFFIX, "La página que buscas no existe o cambió de dirección.", "", body, p, noindex=True)


def redirect_page(target_rel, target_abs):
    return f"""<!doctype html>
<html lang="es-CL"><head><meta charset="utf-8">
<title>Redirigiendo…</title>
<link rel="canonical" href="{target_abs}">
<meta http-equiv="refresh" content="0; url={target_rel}">
<meta name="robots" content="noindex">
</head><body><p>Esta página se movió a <a href="{target_rel}">{target_abs}</a>.</p></body></html>
"""


def main():
    pages = []
    write("", build_home()); pages.append("")
    for builder in (build_services, build_about, build_blog, build_contact):
        path, html = builder(); write(path, html); pages.append(path)
    for s in SERVICES:
        path, html = build_service(s); write(path, html); pages.append(path)
    for x in POSTS:
        path, html = build_post(x); write(path, html); pages.append(path)
    write("404.html", build_404())
    # Redirección de la antigua página de ubicación al contacto
    write("ubicaciones/", redirect_page("../contacto/", SITE + "/contacto/"))
    # URLs antiguas del WordPress que apuntan a servicios existentes
    for old, new in [("policia-local-puerto-montt", "abogados-policia-local-puerto-montt"),
                     ("abogado-de-escrituras-y-contratos-puerto-montt", "redaccion-de-escrituras"),
                     ("asesoria-legal-inmobiliaria-puerto-montt", "asesoria-bienes-raices-puerto-montt")]:
        write(f"portfolio-item/{old}/", redirect_page(f"../{new}/", f"{SITE}/portfolio-item/{new}/"))

    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for path in pages:
            f.write(f"  <url><loc>{SITE}/{path}</loc></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print(f"{len(pages)} páginas generadas + 404 + redirección /ubicaciones/")


if __name__ == "__main__":
    main()

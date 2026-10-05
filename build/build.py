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
        "slug": "abogados-laborales-puerto-montt",
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
            ("Accidentes del trabajo", "Indemnizaciones por accidentes y enfermedades profesionales."),
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
    "abogados-penalistas-puerto-montt": ("Abogados Penalistas en Puerto Montt",
        "Abogados penalistas en Puerto Montt: control de detención, formalización, juicio oral y querellas. Defensa urgente al +56 9 9797 9827.",
        "¿Por qué contar con un abogado penalista?", "Casos penales que atendemos", "defensa penal"),
    "abogados-civiles-puerto-montt": ("Abogados Civiles en Puerto Montt",
        "Abogados civiles en Puerto Montt: juicios de tierras, precario, desalojos, arriendos, cobranzas e indemnizaciones. Agenda tu consulta por WhatsApp.",
        "¿Por qué contar con un abogado civil?", "Juicios civiles que atendemos", "juicios civiles"),
    "abogados-laborales-puerto-montt": ("Abogados Laborales en Puerto Montt",
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

POSTS = [
    {
        "url": SITE + "/2025/11/08/la-accion-de-precario-en-chile/",
        "date": "2025-11-08", "date_txt": "8 de noviembre de 2025", "cat": "Derecho Civil", "icon": "i-home",
        "title": "La acción de precario en Chile",
        "text": "Nadie puede ocupar un inmueble ajeno sin un título que lo justifique. Te explicamos cómo recuperar tu propiedad.",
    },
    {
        "url": SITE + "/2025/08/19/abogados-de-familia-en-puerto-montt-y-region-de-los-lagos/",
        "date": "2025-08-19", "date_txt": "19 de agosto de 2025", "cat": "Familia", "icon": "i-family",
        "title": "Abogados de Familia en Puerto Montt y Región de Los Lagos",
        "text": "Alimentos, divorcio, cuidado personal y medidas de protección: cómo te acompañamos ante los Tribunales de Familia.",
    },
    {
        "url": SITE + "/2025/02/10/corte-suprema-confirma-fallo-que-ordeno-a-beneficiada-restituir-vivienda-serviu/",
        "date": "2025-02-10", "date_txt": "10 de febrero de 2025", "cat": "Jurisprudencia", "icon": "i-news",
        "title": "Corte Suprema confirma fallo que ordenó restituir vivienda SERVIU",
        "text": "El máximo tribunal declaró inadmisible la casación y confirmó la acción reivindicatoria sobre la vivienda.",
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
EXTRA_ICONS = """    <symbol id="i-chev" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="m6 9 6 6 6-6"/></symbol>
    <symbol id="i-info" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></g></symbol>
"""


def wave(amp, period, base, h=80, width=2880):
    d = f"M0 {base}"
    x, up = 0, True
    while x < width:
        cx, x2 = x + period / 4, x + period / 2
        cy = base - amp if up else base + amp
        d += f" Q{cx:g} {cy:g} {x2:g} {base}"
        x, up = x2, not up
    return d + f" V{h} H0 Z"


W1, W2, W3 = wave(14, 360, 30), wave(10, 480, 40), wave(7, 240, 52)


def scene(sea_color):
    """Fondo animado: cielo, aurora, luna, estrellas fugaces, volcanes y mar."""
    return f"""      <div class="grid-bg"></div>
      <div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div>
      <div class="aurora" aria-hidden="true"><i></i><i></i></div>
      <div class="moon" aria-hidden="true"></div>
      <span class="shoot" aria-hidden="true"></span><span class="shoot s2" aria-hidden="true"></span><span class="shoot s3" aria-hidden="true"></span>
      <div class="particles" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
      <div class="landscape" aria-hidden="true">
        <div class="cloud c1"></div><div class="cloud c2"></div><div class="cloud c3"></div>
        <svg class="layer far" data-depth="8" viewBox="0 0 1440 220" preserveAspectRatio="xMidYMax slice">
          <path fill="rgba(169,191,230,.12)" d="M0 190 L70 166 L150 176 L240 146 L330 164 L420 142 L520 168 L610 146 L700 158 L800 136 L900 160 L1000 144 L1100 168 L1200 146 L1300 166 L1380 152 L1440 162 V220 H0Z"/>
        </svg>
        <svg class="layer volcanoes" data-depth="18" viewBox="0 0 1440 220" preserveAspectRatio="xMidYMax slice">
          <defs>
            <linearGradient id="gOsorno" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4d4f2" stop-opacity=".42"/><stop offset="1" stop-color="#7d9ad6" stop-opacity=".14"/></linearGradient>
            <linearGradient id="gCalbuco" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b3c6ec" stop-opacity=".32"/><stop offset="1" stop-color="#7d9ad6" stop-opacity=".1"/></linearGradient>
          </defs>
          <path fill="url(#gOsorno)" d="M430 210 C520 188 600 120 668 56 Q704 28 740 56 C808 120 888 188 978 210 Z"/>
          <path class="snow" fill="rgba(255,255,255,.75)" d="M668 56 Q704 28 740 56 L754 70 L736 80 L721 70 L706 86 L691 70 L675 81 L654 70 Z"/>
          <path fill="url(#gCalbuco)" d="M980 212 L1060 160 L1096 130 L1112 138 L1128 122 L1148 136 L1166 132 L1214 166 L1310 212 Z"/>
          <path fill="rgba(255,255,255,.4)" d="M1096 130 L1112 138 L1128 122 L1148 136 L1166 132 L1177 141 L1157 148 L1140 141 L1120 152 L1104 145 L1087 150 Z"/>
          <ellipse class="smoke" cx="1128" cy="110" rx="16" ry="9" fill="rgba(255,255,255,.35)"/>
          <ellipse class="smoke" cx="1134" cy="104" rx="12" ry="7" fill="rgba(255,255,255,.3)" style="animation-delay:-4.5s"/>
        </svg>
        <svg class="layer near" data-depth="30" viewBox="0 0 1440 220" preserveAspectRatio="xMidYMax slice">
          <path fill="rgba(15,30,61,.6)" d="M0 214 C120 194 220 198 330 205 C460 212 560 190 700 199 C840 208 960 192 1100 203 C1240 212 1340 196 1440 203 V220 H0Z"/>
        </svg>
        <div class="boat"><svg viewBox="0 0 48 32" fill="currentColor"><path d="M23 2v20H9zM25 6l12 16H25z"/><path d="M4 24h40l-5 6H9z"/></svg></div>
        <div class="boat b2"><svg viewBox="0 0 48 32" fill="currentColor"><path d="M23 2v20H9zM25 6l12 16H25z"/><path d="M4 24h40l-5 6H9z"/></svg></div>
        <div class="waves">
          <svg class="w1" viewBox="0 0 2880 80" preserveAspectRatio="none"><path fill="rgba(169,191,230,.12)" d="{W1}"/></svg>
          <svg class="w2" viewBox="0 0 2880 80" preserveAspectRatio="none"><path fill="rgba(255,255,255,.08)" d="{W2}"/></svg>
          <svg class="w3" viewBox="0 0 2880 80" preserveAspectRatio="none"><path fill="{sea_color}" d="{W3}"/></svg>
        </div>
        <div class="glints"><i></i><i></i><i></i><i></i><i></i></div>
      </div>
"""


def area_options(selected=None):
    opts = ['<option value="">Selecciona…</option>']
    for label in ["Familia", "Penal", "Civil", "Laboral", "Herencias / Posesión efectiva", "Policía Local",
                  "Sociedades y empresas", "Contratos y escrituras", "Consulta online", "Otra / No estoy seguro"]:
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


def service_card(s, p, delay=0, detailed=False):
    if detailed:
        body = "<ul>" + "".join(f"<li>{escape(t)}</li>" for t, _ in s["items"][:5]) + "</ul>"
    else:
        body = f"<p>{escape(s['short'])}</p>"
    d = f' style="--d:{delay:.2f}s"' if delay else ""
    return f"""          <article class="service reveal"{d}>
            <div class="ic"><svg><use href="#{s['icon']}"/></svg></div>
            <h3>{escape(s['card'])}</h3>
            {body}
            <div class="actions">
              <a class="go" href="{p}portfolio-item/{s['slug']}/">Ver más<span class="sr-only"> sobre {escape(s['card'])}</span> <svg><use href="#i-arrow"/></svg></a>
              <a class="wa-mini js-wa" data-area="{escape(s['area'])}" data-track="tarjeta-servicio" href="#" aria-label="Consultar por WhatsApp sobre {escape(s['card'])}"><svg><use href="#i-wa"/></svg></a>
            </div>
          </article>"""


def services_grid(p, detailed=False):
    return "\n".join(service_card(s, p, (i % 4) * 0.08, detailed) for i, s in enumerate(SERVICES))


def final_cta():
    return """    <section class="final-cta">
      <div class="orb o1"></div><div class="orb o2"></div>
      <div class="container reveal zoom">
        <h2>¿Necesitas un abogado en Puerto Montt?</h2>
        <p>No dejes pasar los plazos legales. Escríbenos hoy y agenda tu consulta presencial u online.</p>
        <div class="hero-ctas">
          <a class="btn btn-wa js-wa" data-track="final" href="#"><svg><use href="#i-wa"/></svg> Escríbenos por WhatsApp</a>
          <a class="btn btn-light js-call" data-track="final" href="tel:""" + PHONE_TEL + """"><svg><use href="#i-phone"/></svg> Llamar ahora</a>
        </div>
      </div>
    </section>"""


def page_hero(p, crumbs, title, lead, area=None, extra=""):
    items = [f'<li><a href="{p}">Inicio</a></li>']
    for label, href in crumbs:
        items.append(f'<li><a href="{href}">{escape(label)}</a></li>' if href else f'<li aria-current="page">{escape(label)}</li>')
    data_area = f' data-area="{escape(area)}"' if area else ""
    return f"""    <section class="page-hero">
{scene('#ffffff')}
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
{scene('#0f1e3d')}
      <div class="container">
        <div class="hero-in">
          <div class="eyebrow" style="color:var(--accent-2)">Estudio jurídico · Puerto Montt</div>
          <h1>Abogados en Puerto Montt</h1>
          <p class="hero-sub">para proteger
            <span class="rotator">
              <span class="on">a tu familia.</span>
              <span aria-hidden="true">tu libertad.</span>
              <span aria-hidden="true">tu patrimonio.</span>
              <span aria-hidden="true">tu trabajo.</span>
              <span aria-hidden="true">tu empresa.</span>
            </span>
          </p>
          <p class="lead">Asesoría y defensa judicial en familia, penal, civil, laboral, herencias y empresas. Presencial en Puerto Montt y online para todo Chile.</p>
          <div class="hero-ctas">
            <a class="btn btn-wa js-wa" data-track="hero" href="#"><svg><use href="#i-wa"/></svg> Escríbenos por WhatsApp</a>
            <a class="btn btn-ghost js-call" data-track="hero" href="tel:{PHONE_TEL}"><svg><use href="#i-phone"/></svg> {PHONE}</a>
          </div>
          <ul class="trust">
            <li><svg><use href="#i-check"/></svg> Colegio de Abogados</li>
            <li><svg><use href="#i-check"/></svg> Presencial u online</li>
            <li><svg><use href="#i-check"/></svg> Confidencial</li>
          </ul>
        </div>

        <div class="form-wrap">
          <div class="float-badge fb-1"><span class="dot"><svg><use href="#i-wa"/></svg></span><span>Respuesta por WhatsApp<small>en horario hábil</small></span></div>
          <div class="float-badge fb-2"><span class="dot"><svg><use href="#i-video"/></svg></span><span>Consulta online<small>por videollamada</small></span></div>
          {quick_form("form-hero", "Agenda tu consulta", "Déjanos tus datos y te contactamos.", message=False)}
        </div>
      </div>
    </section>

    <div class="marquee" aria-hidden="true">
      <div class="marquee-track">
        {''.join(f'<span>{escape(s["card"])}</span>' for s in SERVICES) * 2}
      </div>
    </div>

    <section class="strip" aria-label="Por qué elegirnos">
      <div class="container">
        <div class="strip-item reveal"><div class="ic"><svg><use href="#i-award"/></svg></div><div><strong>Magíster en Derecho</strong><span>Formación UACh, UC y USS</span></div></div>
        <div class="strip-item reveal" style="--d:.1s"><div class="ic"><svg><use href="#i-pin"/></svg></div><div><strong>Torre del Puerto</strong><span>Oficina en el centro de Puerto Montt</span></div></div>
        <div class="strip-item reveal" style="--d:.2s"><div class="ic"><svg><use href="#i-video"/></svg></div><div><strong>Consultas online</strong><span>Por videollamada, desde todo Chile</span></div></div>
        <div class="strip-item reveal" style="--d:.3s"><div class="ic"><svg><use href="#i-scale"/></svg></div><div><strong>Todas las instancias</strong><span>Juzgados, tribunales y Cortes</span></div></div>
      </div>
    </section>

    <section class="section" id="servicios">
      <div class="container">
        <div class="section-head center reveal">
          <div class="eyebrow">Áreas de práctica</div>
          <h2>¿En qué te podemos ayudar?</h2>
          <p class="lead">Elige tu materia para ver el detalle o escríbenos directo por WhatsApp.</p>
        </div>
        <div class="services cols-3 compact">
{services_grid(p)}
        </div>
      </div>
    </section>

    <section class="section process" id="como-trabajamos">
      <div class="container">
        <div class="section-head center reveal">
          <div class="eyebrow">Cómo trabajamos</div>
          <h2>Agendar tu consulta es simple</h2>
        </div>
        <div class="steps">
          <div class="step reveal"><div class="n">1</div><h3>Escríbenos</h3><p>Por WhatsApp, teléfono o formulario, con un breve resumen de tu situación.</p></div>
          <div class="step reveal" style="--d:.15s"><div class="n">2</div><h3>Coordinamos la reunión</h3><p>Presencial en Torre del Puerto o por videollamada, como te acomode.</p></div>
          <div class="step reveal" style="--d:.3s"><div class="n">3</div><h3>Plan de acción</h3><p>Te explicamos alternativas, plazos y costos, y comenzamos a trabajar.</p></div>
        </div>
      </div>
    </section>

    <section class="section home-about">
      <div class="container about">
        <div class="about-visual reveal left">
          {SCALES}
          <div class="badge">
            <strong>Fernando Calixto Marín</strong>
            <span>Abogado · Fundador del estudio</span>
          </div>
        </div>
        <div class="reveal right">
          <div class="eyebrow">Quiénes somos</div>
          <h2>Experiencia legal al servicio de Puerto Montt</h2>
          <p class="lead">Un equipo de abogados especializados en distintas áreas del derecho, con servicios serios, personalizados y confidenciales.</p>
          <ul class="creds">
            <li><svg><use href="#i-check"/></svg> Magíster en Derecho Privado (UACh) y diplomados UC y USS.</li>
            <li><svg><use href="#i-check"/></svg> Miembro del Colegio de Abogados de Puerto Montt.</li>
            <li><svg><use href="#i-check"/></svg> Apoyo contable para empresas y pymes.</li>
          </ul>
          <a class="btn btn-navy" href="{p}quienes-somos/">Conoce al equipo <svg><use href="#i-arrow"/></svg></a>
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

    <section class="section">
      <div class="container">
        <div class="about">
          <div class="about-visual reveal left">
            {SCALES}
            <div class="badge">
              <strong>Fernando Calixto Marín</strong>
              <span>Abogado · Fundador del estudio</span>
            </div>
          </div>
          <div class="reveal right">
            <div class="eyebrow">Nuestro estudio</div>
            <h2>Servicios legales serios, personalizados y confidenciales</h2>
            <p class="lead">Prestamos servicios y asesorías legales permanentes y ocasionales en Puerto Montt, Puerto Varas y toda la Provincia de Llanquihue.</p>
            <p>El estudio fue fundado por <strong>Fernando Calixto Marín</strong>, abogado dedicado a la asesoría legal y defensa judicial de personas, familias, negocios y empresas de Puerto Montt y la X Región.</p>
            <ul class="creds">
              <li><svg><use href="#i-check"/></svg> Licenciado en Ciencias Jurídicas y Magíster en Derecho Privado (UACh).</li>
              <li><svg><use href="#i-check"/></svg> Diplomados en Derecho Procesal Avanzado y Litigación Oral (UC).</li>
              <li><svg><use href="#i-check"/></svg> Diplomados en Derecho Privado, Derecho Penal Sustantivo y Litigación Oral (USS).</li>
              <li><svg><use href="#i-check"/></svg> Miembro del Colegio de Abogados de Puerto Montt.</li>
            </ul>
          </div>
        </div>
        <!-- Equipo (confirmar nombres y cargos con el estudio) -->
        <div class="team">
{team}
        </div>
      </div>
    </section>

    <section class="section process">
      <div class="container">
        <div class="section-head reveal">
          <div class="eyebrow">Por qué Calixto &amp; Cía.</div>
          <h2>Cercanía, respaldo académico y experiencia en tribunales</h2>
        </div>
        <div class="why-grid">
          <div class="why-item reveal" style="background:#fff"><div class="num">01</div><h3>Trato directo con tu abogado</h3><p>Hablas con quien lleva tu caso. Te explicamos cada etapa en lenguaje simple.</p></div>
          <div class="why-item reveal" style="--d:.1s;background:#fff"><div class="num">02</div><h3>Equipo multidisciplinario</h3><p>Abogados y apoyo contable para abordar tu caso de forma integral.</p></div>
          <div class="why-item reveal" style="--d:.2s;background:#fff"><div class="num">03</div><h3>Presencial u online</h3><p>En nuestra oficina de Torre del Puerto o por videollamada, como te acomode.</p></div>
        </div>
      </div>
    </section>

    <section class="section" style="padding-block:72px">
      <div class="container">
        <div class="section-head center reveal" style="margin-bottom:0">
          <div class="eyebrow">Cobertura</div>
          <h2>Atendemos en toda la Provincia de Llanquihue</h2>
          <p class="lead">Y a clientes de todo el país mediante asesoría online.</p>
          <div class="areas">
            <span class="hl">Puerto Montt</span><span>Puerto Varas</span><span>Llanquihue</span><span>Frutillar</span>
            <span>Los Muermos</span><span>Calbuco</span><span>Maullín</span><span>Fresia</span><span class="hl">Online · todo Chile</span>
          </div>
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
    posts = "\n".join(f"""          <a class="post reveal" style="--d:{i * 0.1:.1f}s" href="{x['url']}">
            <div class="cover"><span class="cat">{escape(x['cat'])}</span><svg><use href="#{x['icon']}"/></svg></div>
            <div class="body">
              <time datetime="{x['date']}">{x['date_txt']}</time>
              <h3>{escape(x['title'])}</h3>
              <p>{escape(x['text'])}</p>
              <span class="read">Leer artículo <svg width="16" height="16"><use href="#i-arrow"/></svg></span>
            </div>
          </a>""" for i, x in enumerate(POSTS))
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
    write("404.html", build_404())
    # Redirección de la antigua página de ubicación al contacto
    write("ubicaciones/", redirect_page("../contacto/", SITE + "/contacto/"))

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

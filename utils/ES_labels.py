import os

def set_labels():
    os.environ['chatbot'] = 'Chatbot de IA'
    os.environ['yes'] = 'Sí'
    os.environ['no'] = 'No'
    os.environ[
        'convo_limit'] = 'Debe completar al menos 5 rondas de conversación, pero puede seguir y completar hasta el máximo de 15.'
    os.environ['intro_wait'] = 'Iniciando chatbot, esto puede tardar hasta 20 segundos...'
    os.environ['react_intro'] = 'Reacción a la introducción:'
    os.environ['intro_emoji'] = 'Select an emoji to continue chatting.'
    os.environ['you'] = 'Usted'
    os.environ['enter'] = 'Presione Enter para enviar'
    os.environ['emoji_prompt'] = 'Reaccione a la respuesta'
    os.environ['finish_chat'] = 'Finalizar chat'
    os.environ['next_page'] = 'Siguiente página'
    os.environ['feedback_page'] = 'Respuestas del chatbot para comentarios'
    os.environ['categories'] = 'Haga clic para saber lo que significa cada categoría'
    os.environ['response'] = 'Respuesta'
    os.environ['user'] = 'Usuario'
    os.environ['give_feedback'] = '¿Hacer comentarios?'
    os.environ['categories_for_response'] = 'Categorías para la respuesta'
    os.environ['comments'] = 'Comentario para la respuesta'
    os.environ['options'] = 'Elija una opción'
    os.environ['comment_prompt'] = 'Agregue su comentario aquí'
    os.environ['submit'] = 'Enviar'
    os.environ[
        'submitted'] = '¡Comentarios enviados! Haga clic en **Ir a la encuesta posterior** para comenzar la encuesta posterior.'

    os.environ['emoji_warning_1'] = 'Para continuar, por favor seleccione un emoji para la respuesta '
    os.environ['emoji_warning_2'] = '.'
    os.environ['convo_update_1'] = 'Ha terminado'
    os.environ['convo_update_2'] = 'ronda(s) de conversación.'
    os.environ['convo_warning_1'] = 'Solo puede hacerle'
    os.environ['convo_warning_2'] = 'pregunta(s) más al chatbot.'
    os.environ[
        'chat_complete'] = "**Chat finalizado.** ¡Gracias por interactuar con el chatbot! A veces, los chatbots generan respuestas inexactas. Presione **Siguiente página** para revisar las respuestas del chatbot y proporcionar comentarios sobre ellas."
    os.environ['comment_outline'] = """
                En esta página, puede proporcionar comentarios sobre las respuestas del chatbot.

                A continuación, verá una lista de pares de entrada/respuesta de su chat. Su entrada está en ***verde*** y la respuesta del chatbot está en ***gris***.

                A la derecha de cada respuesta, puede indicar si desea o no hacer comentarios. 

                Si desea hacer comentarios sobre una respuesta, puede especificar el tipo de comentarios eligiendo entre las categorías del menú desplegable. Puede elegir más de un tipo de comentario. Luego, complete la casilla de comentarios con su opinión sobre la respuesta.

                Debe proporcionar comentarios para al menos dos respuestas del chatbot. Luego de completar el mínimo de dos respuestas, el botón **Enviar** estará habilitado. 

                Haga clic en **Enviar** cuando haya terminado, luego haga clic en **Ir a la encuesta posterior** para realizar la encuesta posterior.
                """
## ***Sistema de Recomendaciones basado en el gusto del usuario***

### *Contexto*
Utilizando la popular plataforma de Streaming "Spotify" que cuenta con millones de usuarios y un catálogo lo suficientemente extenso para satisfacer los gustos de los mas variados usuarios en cuanto a su preferencia musical se refiere, en donde cada uno de ellos pueden crear sus propias playlist, seguir artistas, explorar diferentes géneros musicales, etc. puede volverse un problema encontrar una nueva música que sea de su preferencia.

### *Problemática*
El problema radica en la sobrecarga de información, ya que con tantas opciones disponibles, los usuarios pueden sentirse abrumados y buscar una opción que se adapte a su gusto, puede llevar mucho tiempo y la hasta la frustación del usuario por no encontrar una opción válida.

### *Objetivo*
Desarrollar un sistema de recomendaciones personalizado que ayude a los usuarios a encontrar temas musicales que se ajusten a sus preferencias.

### *Metodología de desarrollo*
- Aplicación del *Algoritmo K-means*
- Aplicación del *Algoritmo DBSCAN*
- Aplicación del *Algoritmo Hierarchical Clustering*
- Aplicación del *Algoritmo Gaussian Mixture Model Clustering*

### *Herramientas utilizadas*
- Sistema Operativo Linux (Ubuntu 22.04)
- Lenguaje de Programación Python
- Proyecto Jupyter Notebook
- Editor de código Visual Studio Code

### *Set de Datos utilizado*
https://www.kaggle.com/datasets/meeraajayakumar/spotify-user-behavior-dataset

### *Descripción del conjunto de datos*
1. *Age* --> Age group of user
2. *Gender* --> Gender of user
3. *spotify_usage_period* --> How long have you been using Spotify
4. *spotify_listening_device* --> Which of the following devices do you primarily use to listen to Spotify?
5.*spotify_subscription_plan* --> Which Spotify subscription plan do you currently have?
6. *premium_sub_willingness* --> Are you willing to take a premium subscription or willing to continue with premium subscription in future?
7. *preffered_premium_plan* --> If premium or willing to take premium, what amount do you pay for the subscription?
8. *preferred_listening_content* --> What do you prefer to listen more?
9. *fav_music_genre* --> What genre(s) of music do you enjoy the most?
10. *music_time_slot* --> What is your favourite time slot to listen to music?
11. *music_Influencial_mood* --> When it comes to listening to music, which of the following moods or situations most strongly influences your choice of music?
12. *music_lis_frequency* --> When do you listen to music more often
13. *music_expl_method* --> How do you discover new music on Spotify
14. *music_recc_rating* --> How do you rate the spotify music recommendations
15. *pod_lis_frequency* --> How often do you listen to Podcast
16. *fav_pod_genre* --> What genre(s) of Podcast do you enjoy the most
17. *preffered_pod_format* --> What podcast format you generally prefer
18. *pod_host_preference* --> Are you more inclined to listen to podcasts from unknown personalities, or do you prefer podcasts hosted by well-known individuals
19. *preffered_pod_duration* --> Do you prefer shorter podcast episodes (under 30 minutes) or longer episodes (over 30 minutes)
20. *pod_variety_satisfaction* --> Are you satisfied with the variety and availability of podcasts on Spotify
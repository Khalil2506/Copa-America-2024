import module as md  # Importa un módulo personalizado
import pandas as pd  
import concat as ct  # Importa otro módulo personalizado para encontrar el player id de los jugadores
import LanusStats as ls  # Importa un módulo específico para estadísticas

# Inicializa una instancia de Fbref para obtener estadísticas de jugadores
fbref = ls.Fbref()
player = fbref.get_player_season_stats('stats', 'Copa America', '2024')  # Obtiene estadísticas de jugadores para la Copa América 2024
player_america = pd.DataFrame(player)  # Convierte las estadísticas a un DataFrame

# Agrega identificadores de jugador al DataFrame usando una función del módulo 'concat'
df_player_america = ct.add_id_player_df(223, 282, player_america)

# Obtiene datos de partidos y estadísticas relacionadas usando funciones del módulo 'module'
match_america = md.match_competition(223, 282)
tarjetas_amarillas_df = md.tarjetas_amarillas_por_partido(223, 282)  # Tarjetas amarillas por partido
df_red = md.card_player(223, 282)  # Tarjetas por jugador (incluye tarjetas rojas)
df_chance_goal = md.player_chance_goal(223, 282)  # Oportunidades de gol por jugador
df_player_dribllle = md.player_dribble_complete(223, 282)  # Dribles completos por partido
df_penalty_player = md.penalty_for_player(223, 282)  # Penales por jugador
df_pass_key = md.pass_key_for_matches(223, 282)  # Pases clave por partido
df_pass = md.pass_for_match(223, 282)  # Pases por partido
df_goal = md.goal_for_player(223, 282)  # Goles por jugador

# Agrupa los datos de goles por jugador y país
df_goal_player = df_goal.groupby(['player', 'country'])['goal'].sum().to_frame()

# Agrupa los datos de asistencias por jugador y país
df_assist = md.assist_player(223, 282)
df_assist_player = df_assist.groupby(['player', 'country'])['assist'].sum().to_frame()

# Agrupa los datos de tiros por jugador y país
df_shot = md.shot_for_player(223, 282)
df_shot_player = df_shot.groupby(['player', 'country'])['shot'].count().to_frame()

df_port = md.porteria_zero(223, 282)  # Datos de porterías a cero
df_minutes = md.calcular_minutos_jugados(223, 282)  # Calcula minutos jugados por jugador
df_match_for_player = md.calcular_partidos_jugados(223, 282)  # Calcula partidos jugados por jugador

# Escribe todos los DataFrames en un archivo Excel con múltiples hojas
with pd.ExcelWriter('Copa_america_2024.xlsx') as writer:
    match_america.to_excel(writer, sheet_name='Match america', index=False)
    df_player_america.to_excel(writer, sheet_name='Player america', index=False)
    df_pass.to_excel(writer, sheet_name='Pases', index=False)
    df_goal.to_excel(writer, sheet_name='Goles Por Jugador', index=False)
    df_assist.to_excel(writer, sheet_name='Asistencias Por Jugador', index=False)
    df_chance_goal.to_excel(writer, sheet_name='Oportunidades de Gol', index=False)
    df_player_dribllle.to_excel(writer, sheet_name='Dribles Completos', index=False)
    df_penalty_player.to_excel(writer, sheet_name='Penales Por Jugador', index=False)
    df_pass_key.to_excel(writer, sheet_name='Pases Clave', index=False)
    df_port.to_excel(writer, sheet_name='Porteria a cero', index=False)
    df_shot.to_excel(writer, sheet_name='Tiro por jugador', index=False)
    df_minutes.to_excel(writer, sheet_name='Minutos por jugador', index=False)
    df_match_for_player.to_excel(writer, sheet_name='partidos por jugador', index=False)
    tarjetas_amarillas_df.to_excel(writer, sheet_name='Tarjetas por Partido', index=False)
    df_red.to_excel(writer, sheet_name='Tarjetas por Jugador', index=False)

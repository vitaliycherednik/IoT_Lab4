from ..entities.agent_data import AgentData
from ..entities.processed_agent_data import ProcessedAgentData


def process_agent_data(agent_data: AgentData) -> ProcessedAgentData:
    road_height = agent_data.accelerometer.z
    if road_height <= 7000:
        road_state = "pothole"  # ямка
    elif 7000 < road_height <= 15000:
        road_state = "smooth road"  # рівна дорога
    else:
        road_state = "bump"  # бугор
    # Створення об'єкту, що містить інформацію про дорогу
    processed_data_batch = ProcessedAgentData(
        road_state=road_state,
        agent_data=agent_data
    )
    return processed_data_batch

import settings

def search_in_json(*keywords):
    data=settings.LEARNING_DATA
    results = []
    keywords = [keyword.lower() for keyword in keywords]  # Преобразуем ключевые слова в нижний регистр для поиска без учета регистра

    def search_dict(d):
        for key, value in d.items():
            if isinstance(value, dict):
                search_dict(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        search_dict(item)
                    elif any(keyword in item.lower() for keyword in keywords):
                        results.append(item)
            elif isinstance(value, str):
                if any(keyword in value.lower() for keyword in keywords):
                    results.append(value)

    search_dict(data)
    return results




                  

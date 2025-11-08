def first():
    GPUs = []
    GPUs_new = GPUs

    gpu_number = int(input("Количество видеокарт: "))

    for i in range(gpu_number):
        GPUs.append(int(input(f"Видеокарта {i+1}: ")))

    print("Старый список видеокарт:", ', '.join(str(GPU) for GPU in GPUs))

    max_gpu_number = None
    for index, GPU in enumerate(GPUs):
        if index == 0:
            max_gpu_number = GPU;
        else:
            if GPU > GPUs[index-1]:
                max_gpu_number = GPU

    for GPU in GPUs_new:
        if GPU == max_gpu_number:
            GPUs_new.remove(GPU)

    print("Новый список видеокарт",', '.join(str(GPU_new) for GPU_new in GPUs_new))

def second():
    films = ["Крепкий орешек",
             "Назад в будущее",
             "Таксист",
             "Леон",
             "Богемская рапсодия",
             "Город грехов",
             "Мементо",
             "Отступники",
             "Деревня"]

    favourite_films = []

    number_of_films = int(input("Сколько фильмов хотите добавить? "))

    for _ in range(number_of_films):
        new_film = input("Введите название фильма: ")
        if new_film in films:
            favourite_films.append(new_film)
        else:
            print(f"Ошибка: фильма {new_film} у нас нет :(")

    print("Ваш список любимых фильмов:", ', '.join(favourite_films))

def third():
    def shifting(initial_list, shift):
        final_list = list(initial_list)
        final_list_temp = list(final_list)

        for _ in range(shift):
            for i, v in enumerate(final_list):
                if i < len(final_list) - 1:
                    final_list_temp[i + 1] = final_list[i]
                else:
                    final_list_temp[-i - 1] = final_list[i]
            final_list = list(final_list_temp)

        return final_list

    initial_list = input("Изначальный список: ").split(", ") # Формат: a, b, c, d, ...
    shift = int(input("Сдвиг: "))
    print("Сдвинуый список:", ', '.join(shifting(initial_list, shift)))
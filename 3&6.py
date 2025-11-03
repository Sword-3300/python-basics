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
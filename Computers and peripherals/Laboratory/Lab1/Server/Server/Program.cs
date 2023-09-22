class PipeServer
{
    static void Main()
    {
        // Открытие каналов
        using NamedPipeServerStream pipeServer = new("channel", PipeDirection.InOut);
        pipeServer.WaitForConnection();

        // Создание сообщения, преобразование в byte
        DataRequest msg = new()
        {
            Number = 1,
            Flag = false
        };

        byte[] bytes = new byte[Unsafe.SizeOf<DataRequest>()];
        Unsafe.As<byte, DataRequest>(ref bytes[0]) = msg;
        pipeServer.Write(bytes, 0, bytes.Length);

        Console.WriteLine($"1. Отправлены данные: num = {msg.Number}, flag = {msg.Flag}");

        // Получение обновленных данных от клиента
        byte[] received_bytes = new byte[Unsafe.SizeOf<DataRequest>()];
        pipeServer.Read(received_bytes, 0, received_bytes.Length);

        DataRequest received_data = Unsafe.As<byte, DataRequest>(ref received_bytes[0]);
        Console.WriteLine($"4. Получен ответ от клиента: num = {received_data.Number}, flag = {received_data.Flag}");
    }
}

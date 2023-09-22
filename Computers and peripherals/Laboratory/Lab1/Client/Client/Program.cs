class PipeClient
{
    static void Main()
    {
        using NamedPipeClientStream pipeClient = new NamedPipeClientStream(".", "channel", PipeDirection.InOut);
        pipeClient.Connect();

        // Получение данных от сервера
        byte[] bytes = new byte[Unsafe.SizeOf<DataRequest>()];
        pipeClient.Read(bytes, 0, bytes.Length);

        DataRequest received_data = Unsafe.As<byte, DataRequest>(ref bytes[0]);
        Console.WriteLine($"2. Получены данные от сервера: num = {received_data.Number}, flag = {received_data.Flag}");

        // Изменение флага
        received_data.Flag = true;

        // Отправка обновленных данных обратно на сервер
        byte[] modified_bytes = new byte[Unsafe.SizeOf<DataRequest>()];
        Unsafe.As<byte, DataRequest>(ref modified_bytes[0]) = received_data;
        pipeClient.Write(modified_bytes, 0, modified_bytes.Length);
        
        Console.WriteLine($"3. Отправлены обновленные данные на сервер: num = {received_data.Number}, flag = {received_data.Flag}");
    }
}

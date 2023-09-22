using System.IO.Pipes;
using System.Runtime.CompilerServices;

public struct Data
{
    public int num;
    public bool flag;
}

class PipeServer
{
    static void Main()
    {
        // Открытие каналов
        using NamedPipeServerStream pipeServer = new("channel", PipeDirection.InOut);
        pipeServer.WaitForConnection();

        StreamWriter sw = new(pipeServer)
        {
            AutoFlush = true
        };

        // Создание сообщения, преобразование в byte
        Data msg = new()
        {
            num = 1,
            flag = false
        };

        byte[] bytes = new byte[Unsafe.SizeOf<Data>()];
        Unsafe.As<byte, Data>(ref bytes[0]) = msg;
        sw.BaseStream.Write(bytes, 0, bytes.Length);

        // Получение обновленных данных от клиента
        byte[] received_bytes = new byte[Unsafe.SizeOf<Data>()];
        sw.BaseStream.Read(received_bytes, 0, received_bytes.Length);
        Data received_data = Unsafe.As<byte, Data>(ref received_bytes[0]);
        Console.WriteLine($"Received data: num = {received_data.num}, flag = {received_data.flag}");
    }
}

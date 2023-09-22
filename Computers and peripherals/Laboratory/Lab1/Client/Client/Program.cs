using System;
using System.IO.Pipes;
using System.Runtime.CompilerServices;

public struct Data
{
    public int num;
    public bool flag;
}

class PipeClient
{
    static void Main()
    {
        using NamedPipeClientStream pipeClient = new NamedPipeClientStream(".", "channel", PipeDirection.InOut);
        pipeClient.Connect();

        StreamReader sr = new StreamReader(pipeClient);

        // Получение данных от сервера
        byte[] bytes = new byte[Unsafe.SizeOf<Data>()];
        sr.BaseStream.Read(bytes, 0, bytes.Length);
        Data received_data = Unsafe.As<byte, Data>(ref bytes[0]);
        Console.WriteLine($"Received data: num = {received_data.num}, flag = {received_data.flag}");

        // Изменение флага
        received_data.flag = true;

        // Отправка обновленных данных обратно на сервер
        byte[] modified_bytes = new byte[Unsafe.SizeOf<Data>()];
        Unsafe.As<byte, Data>(ref modified_bytes[0]) = received_data;
        sr.BaseStream.Write(modified_bytes, 0, modified_bytes.Length);
    }
}

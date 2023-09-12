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
        using NamedPipeClientStream pipeClient = new(".", "channel", PipeDirection.In);
        pipeClient.Connect();

        StreamReader sr = new(pipeClient);
        byte[] bytes = new byte[Unsafe.SizeOf<Data>()];
        sr.BaseStream.Read(bytes, 0, bytes.Length);

        Data msg = new();
        // Unsafe.As<Data,byte>(ref msg) = bytes[0];
        msg = Unsafe.As<byte, Data>(ref bytes[0]);
        Console.WriteLine(msg.num);
    }
}
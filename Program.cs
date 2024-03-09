using System;

public class DatabaseConnection
{
    // Using Lazy<T> for thread-safe lazy initialization
    private static readonly Lazy<DatabaseConnection> instance =
        new Lazy<DatabaseConnection>(() => new DatabaseConnection());

    public DateTime ConnectionTime { get; private set; }

    private DatabaseConnection()
    {
        // Simulating a database connection.
        Console.WriteLine("Connecting to database...");
        // Recording the connection time.
        ConnectionTime = DateTime.Now;
    }

    public static DatabaseConnection Instance
    {
        get
        {
            return instance.Value;
        }
    }

    // Method to demonstrate operation.
    public void Connect()
    {
        Console.WriteLine($"Connection established with the database. Connection time: {ConnectionTime}.");
    }
}

class Program
{
    static void Main(string[] args)
    {
        // First access to the DatabaseConnection instance.
        DatabaseConnection.Instance.Connect();

        // Pause to demonstrate that the connection time remains unchanged.
        System.Threading.Thread.Sleep(2000);

        // Second access to the DatabaseConnection instance.
        DatabaseConnection.Instance.Connect();
    }
}

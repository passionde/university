using Microsoft.Data.Sqlite;
using System.Data;
using static System.ComponentModel.Design.ObjectSelectorEditor;
using static System.Net.Mime.MediaTypeNames;


namespace AccountingClients
{
    internal class DataBase
    {
        SqliteConnection connection = new SqliteConnection("Data Source=C:\\Users\\User\\source\\repos\\Laboratory-works\\Operating Systems\\AccountingClients\\AccountingClients\\DB.db");

        // Получение открытого соединения
        public SqliteConnection GetConnection()
        {
            if (connection.State == System.Data.ConnectionState.Closed)
            {
                connection.Open();
            }

            return connection;
        }
        
        // Форма авторизации
        // Запрос авторизации
        public bool VerificationUser(string loginUser, string passwordUser)
        {
            string sqlExpression = "SELECT * FROM Users WHERE login=@login AND password=@password";
            using (var connection = GetConnection())
            {
                SqliteCommand command = new SqliteCommand(sqlExpression, connection);

                // параметр для логина
                SqliteParameter loginParam = new SqliteParameter("@login", loginUser);
                command.Parameters.Add(loginParam);

                // параметр для пароля
                SqliteParameter passParam = new SqliteParameter("@password", passwordUser);
                command.Parameters.Add(passParam);

                using (SqliteDataReader reader = command.ExecuteReader())
                {
                    return reader.HasRows;
                }
            }
        }

        // Основная форма
        // Запрос информации о всех клиентах
        public DataTable GetInfoClients()
        {
            string sqlExpression = "SELECT * FROM Clients";
            using (var connection = GetConnection())
            {
                SqliteCommand command = new SqliteCommand(sqlExpression, connection);

                DataTable dataTable = new DataTable();

                using (SqliteDataReader reader = command.ExecuteReader())
                {
                    dataTable.Load(reader);
                    return dataTable;
                }
            }
        }

        // Запрос информации о конкретном пользователе
        public string[] GetInfoClient(string clientId)
        {
            string[] response = new string[] { "", "", "", "" };

            DataTable dataTable = new DataTable();

            string sqlExpression = "SELECT FullName, Email, PhoneNumber, DateBirth FROM Clients WHERE ClientId = @clientId;";
            using (var connection = GetConnection())
            {
                SqliteCommand command = new SqliteCommand(sqlExpression, connection);
                command.Parameters.Add(new SqliteParameter("@clientId", clientId));

                using (SqliteDataReader reader = command.ExecuteReader())
                {
                    dataTable.Load(reader);
                    if (dataTable.Rows.Count == 0)
                    {
                        return response;
                    }

                    DataRow dataRow = dataTable.Rows[0];

                    response[0] = dataRow[0].ToString();
                    response[1] = dataRow[1].ToString();
                    response[2] = dataRow[2].ToString();
                    response[3] = dataRow[3].ToString();

                    return response;
                }
            }
        }

        // Запрос информации о наличии пользователя
        public bool IsClient(string clientId)
        {
            string sqlExpression = "SELECT * FROM Clients WHERE ClientId=@clientId";
            using (var connection = GetConnection())
            {
                SqliteCommand command = new SqliteCommand(sqlExpression, connection);

                SqliteParameter loginParam = new SqliteParameter("@clientId", clientId);
                command.Parameters.Add(loginParam);

                using (SqliteDataReader reader = command.ExecuteReader())
                {
                    return reader.HasRows;
                }
            }
        }

        // Запрос на добавление клиента
        public void AddClient(string fullName, string email, string phoneNumber, string dateBirth)
        {
            string sqlExpression = "INSERT INTO Clients (FullName, Email, PhoneNumber, DateBirth, DateAdded) VALUES (@fullName, @email, @phoneNumber, @dateBirth, @DateAdded);";
            using (var connection = GetConnection())
            {
                SqliteCommand command = new SqliteCommand(sqlExpression, connection);

                command.Parameters.Add(new SqliteParameter("@fullName", fullName));
                command.Parameters.Add(new SqliteParameter("@email", email));
                command.Parameters.Add(new SqliteParameter("@phoneNumber", phoneNumber));
                command.Parameters.Add(new SqliteParameter("@dateBirth", dateBirth));
                command.Parameters.Add(new SqliteParameter("@DateAdded", DateTime.Now.ToString("yyyy-MM-dd HH:mm")));

                command.ExecuteNonQuery();
            }
        }

        // Запрос на обновление информации о клиенте
        public void UpdateClientInfo(string clientId, string fullName, string email, string phoneNumber, string dateBirth)
        {
            string sqlExpression = "UPDATE Clients SET FullName = @fullName, Email = @email, PhoneNumber = @phoneNumber, DateBirth = @dateBirth WHERE ClientId = @clientId;";
            using (var connection = GetConnection())
            {
                SqliteCommand command = new SqliteCommand(sqlExpression, connection);

                command.Parameters.Add(new SqliteParameter("@fullName", fullName));
                command.Parameters.Add(new SqliteParameter("@email", email));
                command.Parameters.Add(new SqliteParameter("@phoneNumber", phoneNumber));
                command.Parameters.Add(new SqliteParameter("@dateBirth", dateBirth));
                command.Parameters.Add(new SqliteParameter("@clientId", clientId));

                command.ExecuteNonQuery();
            }
        }

        // Запрос информации о всех сделках
        public DataTable GetOrdersInfo()
        {
            string sqlExpression = "SELECT Orders.OrderId, Orders.OrderDate, Clients.FullName, Clients.Email, Clients.PhoneNumber, Clients.DateBirth, Subscriptions.NameSubscription from Orders, Clients, Subscriptions WHERE Orders.ClientId = Clients.ClientId and Orders.SubscriptionId = Subscriptions.SubscriptionId;";
            using (var connection = GetConnection())
            {
                SqliteCommand command = new SqliteCommand(sqlExpression, connection);

                DataTable dataTable = new DataTable();

                using (SqliteDataReader reader = command.ExecuteReader())
                {
                    dataTable.Load(reader);
                    return dataTable;
                }
            }
        }

        // Запрос текущих наименований абонементов
        public DataTable GetItemsSubs()
        {
            string sqlExpression = "SELECT NameSubscription from Subscriptions;";
            using (var connection = GetConnection())
            {
                SqliteCommand command = new SqliteCommand(sqlExpression, connection);

                DataTable dataTable = new DataTable();

                using (SqliteDataReader reader = command.ExecuteReader())
                {
                    dataTable.Load(reader);
                    return dataTable;
                }
            }
        }

        // Запрос на добавление новой сделки
        public void AddOrder(string clientId, string subscriptionId)
        {
            string sqlExpression = "INSERT INTO Orders (ClientId, SubscriptionId, OrderDate) VALUES (@clientId, @subscriptionId, @orderDate);";
            using (var connection = GetConnection())
            {
                SqliteCommand command = new SqliteCommand(sqlExpression, connection);

                command.Parameters.Add(new SqliteParameter("@clientId", clientId));
                command.Parameters.Add(new SqliteParameter("@subscriptionId", subscriptionId));
                command.Parameters.Add(new SqliteParameter("@orderDate", DateTime.Now.ToString("yyyy-MM-dd HH:mm")));

                command.ExecuteNonQuery();
            }
        }

        // Форма рассылки
        // Запрос данных пользователей подходящих под условие рассылки
        public DataTable GetEmailClientsMailing(decimal countDays)
        {
            string[] response = new string[] {};
            DataTable dataTable = new DataTable();
            string sqlExpression = "SELECT DISTINCT Clients.* " +
                "FROM Orders, Subscriptions, Clients " +
                "WHERE (julianday(Orders.OrderDate, ('+' || CAST(Subscriptions.CountDays as TEXT) || ' days')) - julianday('now') < @countDays) " +
                "AND (julianday(Orders.OrderDate, ('+' || CAST(Subscriptions.CountDays as TEXT) || ' days')) > julianday('now')) " +
                "AND Orders.SubscriptionId = Subscriptions.SubscriptionId " +
                "AND Orders.ClientId = Clients.ClientId;";

            using (var connection = GetConnection())
            {
                SqliteCommand command = new SqliteCommand(sqlExpression, connection);
                command.Parameters.Add(new SqliteParameter("@countDays", Decimal.ToInt32(countDays)));

                using (SqliteDataReader reader = command.ExecuteReader())
                {
                    dataTable.Load(reader);
                    return dataTable;
                }
            }
        }
    }
}

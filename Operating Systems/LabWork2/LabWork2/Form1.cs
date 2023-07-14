using System;

namespace LabWork2
{
    public partial class Form1 : Form
    {
        Mutex mutexRed = new Mutex();
        Mutex mutexBlue = new Mutex();
        Random random = new Random();

        bool finish = false;

        public Form1()
        {
            InitializeComponent();
        }


        void BatleAdd()
        {
            // Добавление бойцов
            while (true) {               

                if (finish)
                {
                    if (Convert.ToInt32(redTeam.Text.ToString()) < Convert.ToInt32(blueTeam.Text.ToString()))
                    {
                        redTeam.Text = "0";
                        MessageBox.Show("Blue team WIN!");
                    }
                    else 
                    {
                        blueTeam.Text = "0";
                        MessageBox.Show("Red team WIN!");
                    }

                    start.Enabled = true;
                    return;
                }

                mutexRed.WaitOne();
                redTeam.Text = Convert.ToString(Convert.ToInt32(redTeam.Text.ToString()) + random.Next(1, 10));
                mutexRed.ReleaseMutex();

                mutexBlue.WaitOne();
                blueTeam.Text = Convert.ToString(Convert.ToInt32(blueTeam.Text.ToString()) + random.Next(1, 10));
                mutexBlue.ReleaseMutex();
            }
        }

        void BatleDel()
        {
            // Удаление бойцов
            while (true)
            {
                mutexRed.WaitOne();
                redTeam.Text = Convert.ToString(Convert.ToInt32(redTeam.Text.ToString()) - random.Next(4, 10));
                mutexRed.ReleaseMutex();

                mutexBlue.WaitOne();
                blueTeam.Text = Convert.ToString(Convert.ToInt32(blueTeam.Text.ToString()) - random.Next(4, 10));
                mutexBlue.ReleaseMutex();

                if (Convert.ToInt32(redTeam.Text.ToString()) <= 0 || Convert.ToInt32(blueTeam.Text.ToString()) <= 0)
                {
                    finish = true;
                    return;
                }
            }
        }

        private void start_Click(object sender, EventArgs e)
        {
            // Проверка пустых полей
            if (redTeam.Text == "" || blueTeam.Text == "")
            {
                MessageBox.Show("Укажите начальный состав команд");
                return;
            }

            // Проверка неправильных полей
            try
            {
                Convert.ToInt32(redTeam.Text);
                Convert.ToInt32(blueTeam.Text);
            }
            catch
            {
                MessageBox.Show("Укажите в качестве начального значения число");
                return;
            }

            // Деактивация кнопки, настройка для новых игр
            start.Enabled = false;
            finish = false;

            // Отключение отслеживания безопасности потоков
            CheckForIllegalCrossThreadCalls = false;

            // Поток для добавления бойцов
            Thread addT = new Thread(BatleAdd);
            addT.Start();

            // Поток для удаления бойцов
            Thread delT = new Thread(BatleDel);
            delT.Start();
            

        }
    }
}
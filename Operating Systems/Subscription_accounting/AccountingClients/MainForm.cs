using System.Data;

namespace AccountingClients
{
    public partial class MainForm : Form
    {
        DataBase dataBase = new DataBase();

        public MainForm()
        {
            InitializeComponent();
        }

        // Закртытие всего приложения при закрытие окна
        private void MainForm_FormClosed(object sender, FormClosedEventArgs e)
        {
            Application.Exit();
        }

        // Перерисовка таблицы с информацией о клиентах
        private void ReloadDataGridViewClients()
        {
            DataTable dt = dataBase.GetInfoClients();
            dataGridView1.DataSource = dt;

        }

        // Перерисовка таблицы с информацией об абонементах
        private void ReloadDataGridViewOrders()
        {
            DataTable dt = dataBase.GetOrdersInfo();
            dataGridView2.DataSource = dt;

        }

        // Начальная прорисовка основных элементов при загрузке окна
        private void MainForm_Load(object sender, EventArgs e)
        {
            ReloadDataGridViewClients(); // Таблица клиентов
            ReloadDataGridViewOrders(); // Таблица абонементов

            // Список доступных абонементов
            DataTable dt = dataBase.GetItemsSubs();
            foreach (DataRow row in dt.Rows)
            {
                subsType.Items.Add(row[0]);
            }
            subsType.SelectedIndex = 0;

        }

        // Изменение активности кнопки добавления клиента в зависимости от валидности данных
        private void EnabledButtonAddClients()
        {
            buttonAdd.Enabled = false;

            if (textBox1.Text != "" && textBox2.Text != "" && textBox3.Text != "")
            {
                buttonAdd.Enabled = true;
            }
        }

        // Изменение активности кнопки изменения информации о клиента в зависимости от валидности данных
        private void EnabledButtonUpdateClient()
        {
            button1.Enabled = false;

            if (textBox11.Text != "" && textBox8.Text != "" && textBox10.Text != "" && textBox9.Text != "")
            {
                button1.Enabled = true;
            }
        }
                
        // Добавление нового клиента
        private void buttonAdd_Click(object sender, EventArgs e)
        {
            dataBase.AddClient(textBox1.Text, textBox2.Text, textBox3.Text, dateTimePicker1.Value.ToString("yyyy-MM-dd"));

            MessageBox.Show($"Пользователь {textBox1.Text} добавлен");

            textBox1.Text = "";
            textBox2.Text = "";
            textBox3.Text = "";
            dateTimePicker1.Value = DateTime.Now;

            buttonAdd.Enabled = false;

            ReloadDataGridViewClients();
        }

        // Добавления новой покупки абонемента
        private void buttonAddOrder_Click(object sender, EventArgs e)
        {
            dataBase.AddOrder(textBox5.Text, (subsType.SelectedIndex + 1).ToString());

            MessageBox.Show("Новая заявка успешно добавлена");
                        
            subsType.SelectedIndex = 0;

            textBox5.Text = "";
            textBox4.Text = "";
            textBox6.Text = "";
            textBox7.Text = "";

            buttonAddOrder.Enabled = false;

            ReloadDataGridViewOrders();
        }

        // Обновление данных пользователя
        private void button1_Click(object sender, EventArgs e)
        {
            if (!dataBase.IsClient(textBox9.Text))
            {
                textBox9.Text = "";
                MessageBox.Show("Клиента с таким ID не существует");
                return;
            }
            dataBase.UpdateClientInfo(textBox9.Text, textBox11.Text, textBox10.Text, textBox8.Text, dateTimePicker2.Value.ToString("yyyy-MM-dd"));

            MessageBox.Show($"Данные пользователя {textBox11.Text} успешно изменены");

            textBox9.Text = "";

            buttonAdd.Enabled = false;

            ReloadDataGridViewClients();
            ReloadDataGridViewOrders();
        }

        // Реализация поиска клиента при изменении поля
        private void textBox8_TextChanged(object sender, EventArgs e)
        {      
            for (int i = 0; i < dataGridView1.RowCount; i++)
            {
                dataGridView1.Rows[i].Selected = false;
                for (int j = 0; j < dataGridView1.ColumnCount; j++)
                    if (dataGridView1.Rows[i].Cells[j].Value != null)
                        if (dataGridView1.Rows[i].Cells[j].Value.ToString().ToLower().Contains(SearchClientFullName.Text.ToLower()))
                        {
                            dataGridView1.Rows[i].Selected = true;
                            break;
                        }
            }
        }

        // Отмена выделения строк после поиска клиента (если строка поиска пуста)
        private void SearchClientFullName_Leave(object sender, EventArgs e)
        {
            if (SearchClientFullName.Text == "")
            {
                for (int i = 0; i < dataGridView1.RowCount; i++)
                {
                    dataGridView1.Rows[i].Selected = false;
                }
            }
        }        

        // Загрузка данных о пользователе при добавлении нового абонемента (после ввода Id загружаются данные)
        private void textBox5_TextChanged(object sender, EventArgs e)
        {
            buttonAddOrder.Enabled = false;
            string[] response = dataBase.GetInfoClient(textBox5.Text);

            if (response[0] != "")
            {
                buttonAddOrder.Enabled = true;
            }

            textBox4.Text = response[0];
            textBox6.Text = response[2];
            textBox7.Text = response[3];
        }

        // Загрузка данных о пользователе при добавлении изменении информации о нем (после ввода Id загружаются данные)
        private void textBox9_TextChanged(object sender, EventArgs e)
        {
            string[] response = dataBase.GetInfoClient(textBox9.Text);

            if (response[0] != "")
            {
                buttonAddOrder.Enabled = true;
            }

            textBox11.Text = response[0];
            textBox10.Text = response[1];
            textBox8.Text = response[2];
            if (response[3] != "")
            {
                dateTimePicker2.Value = DateTime.ParseExact(response[3].ToString(), "yyyy-MM-dd", null);
            }
        }

        // Загрузка формы настройки оповещения пользователей
        private void опощениеОбИстеченииАбонементаToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Mailing mailing = new Mailing();
            mailing.ShowDialog();
        }

        

        // Связка функций для изменения активности кнопки
        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            EnabledButtonAddClients();
        }
        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            EnabledButtonAddClients();
        }
        private void textBox3_TextChanged(object sender, EventArgs e)
        {
            EnabledButtonAddClients();
        }

        private void textBox11_TextChanged(object sender, EventArgs e)
        {
            EnabledButtonUpdateClient();
        }
        private void textBox10_TextChanged(object sender, EventArgs e)
        {
            EnabledButtonUpdateClient();
        }
        private void textBox8_TextChanged_1(object sender, EventArgs e)
        {
            EnabledButtonUpdateClient();
        }

        
    }
}

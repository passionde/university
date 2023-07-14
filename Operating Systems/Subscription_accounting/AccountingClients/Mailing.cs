using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Mail;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;
using Microsoft.VisualBasic.Logging;

namespace AccountingClients
{
    public partial class Mailing : Form
    {
        DataBase dataBase = new DataBase();
        public Mailing()
        {
            InitializeComponent();
        }

        private async Task SendEmailAsync()
        {
            var fromAddress = new MailAddress("YOUR EMAIL", "Тренажерный зал");
            const string fromPassword = "YOUR PASSWORD";
            const string subject = "Оповещение о необходимости продления абонемента";
            string body = textBox1.Text.ToString();

            var smtp = new SmtpClient
            {
                Host = "smtp.gmail.com",
                Port = 587,
                EnableSsl = true,
                DeliveryMethod = SmtpDeliveryMethod.Network,
                UseDefaultCredentials = false,
                Credentials = new NetworkCredential(fromAddress.Address, fromPassword)
            };

            foreach (DataGridViewRow r in dataGridView1.Rows)
            {
                var toAddress = new MailAddress(r.Cells["Email"].Value.ToString());

                using (var message = new MailMessage(fromAddress, toAddress)
                {
                    Subject = subject,
                    Body = body
                })
                {
                    try
                    {
                        await smtp.SendMailAsync(message);
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show("err: " + ex.Message);
                    }
                }
            }
        }

        private void buttonSend_Click(object sender, EventArgs e)
        {
            SendEmailAsync().GetAwaiter();
            MessageBox.Show($"Рассылка закончена. Всего оповещено: {dataGridView1.RowCount}");
            

        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            DataTable dt = dataBase.GetEmailClientsMailing(numericUpDown1.Value);
            dataGridView1.DataSource = dt;

            if (dataGridView1.Rows.Count > 0)
            {
                buttonSend.Enabled = true;
            }
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            if (textBox1.Text.ToString() == "")
            {
                buttonSend.Enabled = false;
            }
        }
    }
}

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
            // ���������� ������
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
            // �������� ������
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
            // �������� ������ �����
            if (redTeam.Text == "" || blueTeam.Text == "")
            {
                MessageBox.Show("������� ��������� ������ ������");
                return;
            }

            // �������� ������������ �����
            try
            {
                Convert.ToInt32(redTeam.Text);
                Convert.ToInt32(blueTeam.Text);
            }
            catch
            {
                MessageBox.Show("������� � �������� ���������� �������� �����");
                return;
            }

            // ����������� ������, ��������� ��� ����� ���
            start.Enabled = false;
            finish = false;

            // ���������� ������������ ������������ �������
            CheckForIllegalCrossThreadCalls = false;

            // ����� ��� ���������� ������
            Thread addT = new Thread(BatleAdd);
            addT.Start();

            // ����� ��� �������� ������
            Thread delT = new Thread(BatleDel);
            delT.Start();
            

        }
    }
}
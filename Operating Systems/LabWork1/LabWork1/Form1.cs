namespace LabWork1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            textBox1.Text = Environment.OSVersion.VersionString.ToString();

            if (Environment.Is64BitOperatingSystem)
            {
                textBox2.Text = "x64";
            } else
            {
                textBox2.Text = "x32";
            }

            textBox4.Text = Environment.SystemDirectory.ToString();

            textBox3.Text = Environment.UserDomainName;
            textBox5.Text = Environment.UserName;
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            
        }
    }
}
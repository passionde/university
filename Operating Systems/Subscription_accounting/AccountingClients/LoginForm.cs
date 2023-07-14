namespace AccountingClients
{
    public partial class LoginForm : Form
    {
        MainForm mainForm = new MainForm();
        public LoginForm()
        {
            InitializeComponent();
        }

        private void buttonLogin_Click(object sender, EventArgs e)
        {
            DataBase db = new DataBase();

            string loginUser = loginField.Text;
            string passwordUser = passwordField.Text;

            if (db.VerificationUser(loginUser, passwordUser))
            {
                mainForm.Show();
                this.Hide();
            }
            else
            {
                passwordField.Text = "";
                passwordField.PlaceholderText = "Invalid password";
            }
        }
    }
}

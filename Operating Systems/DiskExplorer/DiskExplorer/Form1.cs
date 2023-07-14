using System.Diagnostics;
using System.Security;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace DiskExplorer
{
    public partial class Form1 : Form
    {

        string currentPath = @"C:\\";
        Thread threadSearch;
        Mutex mutexObj = new Mutex();
        string searchString = "";
        List<string> fullPathItems = new List<string>();
        

        public Form1()
        {
            InitializeComponent();
        }

        // Функция поиска и отображения данных
        void search()
        {
            mutexObj.WaitOne();
            

            listDirectories.Items.Clear();  // Очистка listBox
            fullPathItems.Clear();  // Очитска списка с полными путями
            listDirectories.View = View.List;  // Изменение способа отображения
            textBoxCurrentPath.Text = "    Search results";

            foreach (FileInfo fileName in SafeSearch.EnumerateFiles(currentPath, $"{textBoxSearc.Text.ToLower()}*"))
            {
                if (textBoxSearc.Text == "")
                {
                    viewList();
                    mutexObj.ReleaseMutex();
                    return;
                }

                if (searchString != textBoxSearc.Text || listDirectories.Items.Count >= 100)
                {
                    mutexObj.ReleaseMutex();
                    return;
                }

                listDirectories.Items.Add(fileName.Name.ToString());
                fullPathItems.Add(fileName.FullName);

            }

            mutexObj.ReleaseMutex();


        }

        // Функция перерисовки текущего каталога
        private void viewList()
        {
            DirectoryInfo dInfo = new DirectoryInfo(currentPath);
            ImageList images = new ImageList();
            FileInfo[] files = dInfo.GetFiles();

            listDirectories.Items.Clear();
            fullPathItems.Clear();  // Очитска списка с полными путями
            listDirectories.View = View.LargeIcon;

            // Добавление картинок файлов
            for (int i = 0; i < files.GetLength(0); i++)
            {
                images.Images.Add(files[i].Extension, Icon.ExtractAssociatedIcon(files[i].FullName));
            }

            // Добавление картинки для папки
            images.Images.Add("Folder", new Icon("C:\\Users\\User\\source\\repos\\DiskExplorer\\DiskExplorer\\Icons\\Hopstarter-Sleek-Xp-Basic-Folder.ico"));
            
            // Установка набора картинок
            listDirectories.LargeImageList = images;
            listDirectories.SmallImageList = images;

            // Добавление файлов в list
            for (int i = 0; i < files.GetLength(0); i++)
            {
                listDirectories.Items.Add(files[i].Name, images.Images.IndexOfKey(files[i].Extension));
                fullPathItems.Add(files[i].FullName.ToString());
            }

            // Добавление каталогов в list
            foreach (DirectoryInfo directoryInfo in dInfo.GetDirectories())
            {
                listDirectories.Items.Add(directoryInfo.Name, images.Images.IndexOfKey("Folder"));
                fullPathItems.Add(directoryInfo.FullName);
            }

            // Изменение строчки текущего пути
            textBoxCurrentPath.Text = "    " + currentPath;

        }

        // Отображение корневой папки
        private void Form1_Load(object sender, EventArgs e)
        {
            viewList();
        }

        // Возвращение на предыдущий каталог
        private void buttonBack_Click(object sender, EventArgs e)
        {
            DirectoryInfo dInfo = new DirectoryInfo(currentPath);
            if (dInfo.Parent == null || textBoxSearc.Text != "")
            {
                return;
            }
            currentPath = dInfo.Parent.FullName + "\\";
            viewList();
        }

        // Отображение выбранной папки при двойном нажатии
        private void listDirectories_DoubleClick(object sender, EventArgs e)
        {            
            string newPath = currentPath + listDirectories.SelectedItems[0].Text + "\\";

            if (Directory.Exists(newPath))
            {
                string tmp = currentPath;
                try
                {
                    currentPath = newPath;
                    viewList();
                }
                catch
                {
                    MessageBox.Show("Отказано в доступе");
                    currentPath = tmp;
                }
                
            }
        }

        private void textBoxSearc_TextChanged(object sender, EventArgs e)
        {
            CheckForIllegalCrossThreadCalls = false;

            searchString = textBoxSearc.Text;

            threadSearch = new Thread(search);
            threadSearch.Start();
        }

        private void listDirectories_MouseClick(object sender, MouseEventArgs e)
        {
            if (e.Button != MouseButtons.Right)
            {
                return;
            }

            string path = fullPathItems[listDirectories.SelectedIndices[0]];

            Form propForm = new PropFile(path);
        }
    }
}
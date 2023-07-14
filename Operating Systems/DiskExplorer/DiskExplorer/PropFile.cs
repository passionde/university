using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Net.WebRequestMethods;

namespace DiskExplorer
{
    public partial class PropFile : Form
    {
        public PropFile(string path)
        {
            InitializeComponent();

            try
            {
                if (Directory.Exists(path))
                {
                    DirectoryInfo directoryInfo = new DirectoryInfo(path);
                    title.Text = directoryInfo.Name;
                    type.Text = "Папка с файлами";
                    location.Text = directoryInfo.FullName;

                    long totalSize = 0;
                    foreach (FileInfo file in directoryInfo.GetFiles())
                    {
                        file.Refresh();
                        totalSize += file.Length;
                    }
                    size.Text = $"{(totalSize % 1024).ToString()} КБ ({totalSize.ToString()} байт)";

                    dateCreate.Text = directoryInfo.CreationTime.ToString();
                    lastModifed.Text = directoryInfo.LastWriteTime.ToString();
                }
                else
                {
                    FileInfo fileInfo = new FileInfo(path);
                    fileInfo.Refresh();
                    title.Text = fileInfo.Name;
                    type.Text = "Файл";
                    location.Text = fileInfo.FullName;

                    size.Text = $"{(fileInfo.Length % 1024).ToString()} КБ ({fileInfo.Length.ToString()} байт)";

                    dateCreate.Text = fileInfo.CreationTime.ToString();
                    lastModifed.Text = fileInfo.LastWriteTime.ToString();
                }

                this.Show();
            }
            catch
            {
                MessageBox.Show("Отказано в доступе");
            }
            
        }
    }
}

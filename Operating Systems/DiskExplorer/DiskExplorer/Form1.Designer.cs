namespace DiskExplorer
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.listDirectories = new System.Windows.Forms.ListView();
            this.panel1 = new System.Windows.Forms.Panel();
            this.textBoxCurrentPath = new System.Windows.Forms.TextBox();
            this.buttonBack = new System.Windows.Forms.Button();
            this.textBoxSearc = new System.Windows.Forms.TextBox();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // listDirectories
            // 
            this.listDirectories.Alignment = System.Windows.Forms.ListViewAlignment.SnapToGrid;
            this.listDirectories.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.listDirectories.Location = new System.Drawing.Point(0, 49);
            this.listDirectories.MultiSelect = false;
            this.listDirectories.Name = "listDirectories";
            this.listDirectories.Size = new System.Drawing.Size(867, 428);
            this.listDirectories.TabIndex = 1;
            this.listDirectories.UseCompatibleStateImageBehavior = false;
            this.listDirectories.DoubleClick += new System.EventHandler(this.listDirectories_DoubleClick);
            this.listDirectories.MouseClick += new System.Windows.Forms.MouseEventHandler(this.listDirectories_MouseClick);
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.textBoxCurrentPath);
            this.panel1.Controls.Add(this.buttonBack);
            this.panel1.Controls.Add(this.textBoxSearc);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Top;
            this.panel1.Location = new System.Drawing.Point(0, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(867, 48);
            this.panel1.TabIndex = 2;
            // 
            // textBoxCurrentPath
            // 
            this.textBoxCurrentPath.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right)));
            this.textBoxCurrentPath.Enabled = false;
            this.textBoxCurrentPath.Location = new System.Drawing.Point(45, 12);
            this.textBoxCurrentPath.Name = "textBoxCurrentPath";
            this.textBoxCurrentPath.Size = new System.Drawing.Size(597, 27);
            this.textBoxCurrentPath.TabIndex = 3;
            // 
            // buttonBack
            // 
            this.buttonBack.Anchor = System.Windows.Forms.AnchorStyles.Left;
            this.buttonBack.BackColor = System.Drawing.Color.Transparent;
            this.buttonBack.BackgroundImage = global::DiskExplorer.Properties.Resources.back;
            this.buttonBack.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.buttonBack.Location = new System.Drawing.Point(12, 12);
            this.buttonBack.Name = "buttonBack";
            this.buttonBack.Size = new System.Drawing.Size(27, 27);
            this.buttonBack.TabIndex = 1;
            this.buttonBack.UseVisualStyleBackColor = false;
            this.buttonBack.Click += new System.EventHandler(this.buttonBack_Click);
            // 
            // textBoxSearc
            // 
            this.textBoxSearc.Anchor = System.Windows.Forms.AnchorStyles.Right;
            this.textBoxSearc.Location = new System.Drawing.Point(648, 12);
            this.textBoxSearc.Name = "textBoxSearc";
            this.textBoxSearc.PlaceholderText = "Поиск в текущем каталоге";
            this.textBoxSearc.Size = new System.Drawing.Size(207, 27);
            this.textBoxSearc.TabIndex = 2;
            this.textBoxSearc.TextChanged += new System.EventHandler(this.textBoxSearc_TextChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(867, 477);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.listDirectories);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private ListView listDirectories;
        private Panel panel1;
        private TextBox textBoxSearc;
        private Button buttonBack;
        private TextBox textBoxCurrentPath;
    }
}
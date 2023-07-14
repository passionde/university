#include "lab04_sqlite.h"

#include <gtk/gtk.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define UI_FILE "lab04.glade"

enum
{
    ANIMAL_ID = 0,
    KLICHKA,
    DATE,
    POL,
    VID_ID,
    VID,
    KORM_ID,
    KORM
};

struct MainWindowObjects
{
    GtkWindow *main_window;
    GtkTreeView *treeview;
    GtkListStore *liststore;
    GtkAdjustment *adjustment;
    GtkTreeViewColumn *column_animal_id;
    GtkTreeViewColumn *column_klichka;
    GtkTreeViewColumn *column_date_of_birth;
    GtkTreeViewColumn *column_pol;
    GtkTreeViewColumn *column_vid_id;
    GtkTreeViewColumn *column_korm_id;
    GtkTextView *lbl_klichka;
    GtkTextView *lbl_date_of_birth;
    GtkTextView *lbl_pol;
    GtkTextView *lbl_vid;
    GtkTextView *lbl_korm;
} mainWindowObjects;

int flag = 1;

int callback(void *not_used, int argc, char **argv, char **col_names)
{
    GtkTreeIter iter;
    
    if (argc == 8)
    {
        gtk_list_store_append(GTK_LIST_STORE(mainWindowObjects.liststore), &iter);
        gtk_list_store_set(GTK_LIST_STORE(mainWindowObjects.liststore), &iter, ANIMAL_ID,
                           atoi(argv[ANIMAL_ID]), KLICHKA, argv[KLICHKA], DATE, argv[DATE], POL, argv[POL],
                           VID_ID, atoi(argv[VID_ID]), VID, argv[VID], KORM_ID, atoi(argv[KORM_ID]), KORM, argv[KORM], -1);
    }
    return 0;
}



int main(int argc, char **argv)
{
    GtkBuilder *builder;
    GError *error = NULL;
    gtk_init(&argc, &argv);

    builder = gtk_builder_new();

    if (!gtk_builder_add_from_file(builder, UI_FILE, &error))
    {
        g_warning("%s\n", error->message);
        g_free(error);
        return (1);
    }

    mainWindowObjects.main_window = GTK_WINDOW(gtk_builder_get_object(builder, "main_window"));
    mainWindowObjects.treeview =
        GTK_TREE_VIEW(gtk_builder_get_object(builder, "treeview_components"));
    mainWindowObjects.liststore =
        GTK_LIST_STORE(gtk_builder_get_object(builder, "liststore_components"));

    mainWindowObjects.column_klichka =
        GTK_TREE_VIEW_COLUMN(gtk_builder_get_object(builder, "cln_klichka"));

    mainWindowObjects.column_date_of_birth =
        GTK_TREE_VIEW_COLUMN(gtk_builder_get_object(builder, "cln_date_of_birth"));
    mainWindowObjects.column_pol =
        GTK_TREE_VIEW_COLUMN(gtk_builder_get_object(builder, "cln_pol"));
    mainWindowObjects.column_animal_id =
        GTK_TREE_VIEW_COLUMN(gtk_builder_get_object(builder, "cln_animal_id"));
    mainWindowObjects.column_vid_id =
        GTK_TREE_VIEW_COLUMN(gtk_builder_get_object(builder, "cln_vid_id"));
    mainWindowObjects.column_korm_id =
        GTK_TREE_VIEW_COLUMN(gtk_builder_get_object(builder, "cln_korm_id"));
    mainWindowObjects.lbl_klichka = GTK_TEXT_VIEW(gtk_builder_get_object(builder, "lbl_klichka"));
    mainWindowObjects.lbl_date_of_birth = GTK_TEXT_VIEW(gtk_builder_get_object(builder, "lbl_date"));
    mainWindowObjects.lbl_pol = GTK_TEXT_VIEW(gtk_builder_get_object(builder, "lbl_pol"));
    mainWindowObjects.lbl_vid = GTK_TEXT_VIEW(gtk_builder_get_object(builder, "lbl_vid"));
    mainWindowObjects.lbl_korm = GTK_TEXT_VIEW(gtk_builder_get_object(builder, "lbl_korm"));
    gtk_builder_connect_signals(builder, &mainWindowObjects);
    
    g_object_unref(G_OBJECT(builder));
    gtk_widget_show_all(GTK_WIDGET(mainWindowObjects.main_window));

    sqlite_get_data(1);

    gtk_main();
}

G_MODULE_EXPORT void on_btnsave_clicked(GtkWidget *button, gpointer data)
{
    GtkTreeIter iter;
    gboolean reader =
        gtk_tree_model_get_iter_first(GTK_TREE_MODEL(mainWindowObjects.liststore), &iter);
    while (reader)
    {
         
        gint animalid;
        gchar *klichka;
        gchar *date;
        gchar *pol;
        gint vid_id;
        gint korm_id;
        
        gtk_tree_model_get(GTK_TREE_MODEL(mainWindowObjects.liststore), &iter, ANIMAL_ID, &animalid,
                           KLICHKA, &klichka, DATE, &date, POL, &pol, VID_ID, &vid_id, KORM_ID, &korm_id, -1);
        sqlite_update(animalid, klichka, date, pol, vid_id, korm_id);
        reader = gtk_tree_model_iter_next(GTK_TREE_MODEL(mainWindowObjects.liststore), &iter);
    }
    gtk_list_store_clear(mainWindowObjects.liststore);
    sqlite_get_data(1);
}

G_MODULE_EXPORT void on_btn_add_clicked(GtkWidget *button, gpointer data)
{
    int vid_id, korm_id;
    GtkTextIter start, end;
    GtkTextBuffer *buffer = gtk_text_view_get_buffer(mainWindowObjects.lbl_klichka);
    gchar *klichka, *date, *pol, *vid, *korm;
    gtk_text_buffer_get_bounds(buffer, &start, &end);
    klichka = gtk_text_buffer_get_text(buffer, &start, &end, FALSE);
    buffer = gtk_text_view_get_buffer(mainWindowObjects.lbl_date_of_birth);
    gtk_text_buffer_get_bounds(buffer, &start, &end);
    date = gtk_text_buffer_get_text(buffer, &start, &end, FALSE);
    buffer = gtk_text_view_get_buffer(mainWindowObjects.lbl_pol);
    gtk_text_buffer_get_bounds(buffer, &start, &end);
    pol = gtk_text_buffer_get_text(buffer, &start, &end, FALSE);
    buffer = gtk_text_view_get_buffer(mainWindowObjects.lbl_vid);
    gtk_text_buffer_get_bounds(buffer, &start, &end);
    vid = gtk_text_buffer_get_text(buffer, &start, &end, FALSE);
    buffer = gtk_text_view_get_buffer(mainWindowObjects.lbl_korm);
    gtk_text_buffer_get_bounds(buffer, &start, &end);
    korm = gtk_text_buffer_get_text(buffer, &start, &end, FALSE);
    if (!strcmp(vid, "Рыба")) vid_id = 3;
        else if (!strcmp(vid, "Комар")) vid_id = 2;
        else vid_id = 1;
    if (!strcmp(korm, "Натуральный")) korm_id = 3;
        else if (!strcmp(korm, "Мокрый")) korm_id = 2;
        else korm_id = 1;
    sqlite_insert(klichka, date, pol, vid_id, korm_id);
    gtk_list_store_clear(GTK_LIST_STORE(mainWindowObjects.liststore));
    sqlite_get_data(1);
}

G_MODULE_EXPORT void on_btn_del_clicked(GtkWidget *button, gpointer data)
{
    GList *_list;
	GtkTreeIter iter;
	GtkTreeModel *model;
	GtkTreeSelection *sel;


	sel = gtk_tree_view_get_selection(mainWindowObjects.treeview);

	for(_list = gtk_tree_selection_get_selected_rows(sel, &model); _list; _list = g_list_next(_list))
	{
		GtkTreePath *path = _list->data;
		int animal_id;

		gtk_tree_model_get_iter(model, &iter, path);
		gtk_tree_model_get(model, &iter, ANIMAL_ID, &animal_id, -1);
        sqlite_delete(animal_id);
	}

	g_list_foreach(_list, (GFunc)gtk_tree_path_free, NULL);
	g_list_free(_list);
    gtk_list_store_clear(GTK_LIST_STORE(mainWindowObjects.liststore));
    sqlite_get_data(1);
}

G_MODULE_EXPORT void on_klichka_edited(GtkCellRendererText *renderer, gchar *path,
                                                         gchar *new_text, gpointer data)
{
    if (g_ascii_strcasecmp(new_text, "") != 0)
    {
        GtkTreeIter iter;
        GtkTreeModel *model;
        model = gtk_tree_view_get_model(mainWindowObjects.treeview);
        if (gtk_tree_model_get_iter_from_string(model, &iter, path))
            gtk_list_store_set(GTK_LIST_STORE(model), &iter, KLICHKA, new_text, -1);
    }
}

G_MODULE_EXPORT void on_date_of_birth_edited(GtkCellRendererText *renderer, gchar *path,
                                                         gchar *new_text, gpointer data)
{
    if (g_ascii_strcasecmp(new_text, "") != 0)
    {
        GtkTreeIter iter;
        GtkTreeModel *model;
        model = gtk_tree_view_get_model(mainWindowObjects.treeview);
        if (gtk_tree_model_get_iter_from_string(model, &iter, path))
            gtk_list_store_set(GTK_LIST_STORE(model), &iter, DATE, new_text, -1);
    }
}

G_MODULE_EXPORT void on_pol_edited(GtkCellRendererText *renderer, gchar *path,
                                                         gchar *new_text, gpointer data)
{
    if (g_ascii_strcasecmp(new_text, "") != 0)
    {
        GtkTreeIter iter;
        GtkTreeModel *model;
        model = gtk_tree_view_get_model(mainWindowObjects.treeview);
        if (gtk_tree_model_get_iter_from_string(model, &iter, path))
            gtk_list_store_set(GTK_LIST_STORE(model), &iter, POL, new_text, -1);
    }
}

G_MODULE_EXPORT void on_vid_edited(GtkCellRendererText *renderer, gchar *path,
                                                      gchar *new_text, gpointer data)
{
    if (g_ascii_strcasecmp(new_text, "") != 0)
    {
        int id;
        GtkTreeIter iter;
        GtkTreeModel *model;
        model = gtk_tree_view_get_model(mainWindowObjects.treeview);
        if (!strcmp(new_text, "Кот")) id = 1;
        else if (!strcmp(new_text, "Комар")) id = 2;
        else id = 3;
        if (gtk_tree_model_get_iter_from_string(model, &iter, path))
            gtk_list_store_set(GTK_LIST_STORE(model), &iter, VID, new_text, VID_ID, id, -1);
    }
}

G_MODULE_EXPORT void on_korm_edited(GtkCellRendererText *renderer, gchar *path,
                                                      gchar *new_text, gpointer data)
{
    if (g_ascii_strcasecmp(new_text, "") != 0)
    {
        int id;
        GtkTreeIter iter;
        GtkTreeModel *model;
        model = gtk_tree_view_get_model(mainWindowObjects.treeview);
        if (!strcmp(new_text, "Сухой")) id = 1;
        else if (!strcmp(new_text, "Мокрый")) id = 2;
        else id = 3;
        if (gtk_tree_model_get_iter_from_string(model, &iter, path))
            gtk_list_store_set(GTK_LIST_STORE(model), &iter, KORM, new_text, KORM_ID, id, -1);
    }
}

G_MODULE_EXPORT void on_show_hidden_toggled(GtkToggleButton *button, gpointer data)
{
    if (!flag)
    {
        flag = 1;
        gtk_list_store_clear(GTK_LIST_STORE(mainWindowObjects.liststore));
        sqlite_get_data(flag);
    }
    else{
        flag = 0;
        gtk_list_store_clear(GTK_LIST_STORE(mainWindowObjects.liststore));
        sqlite_get_data(flag);
    }
}

G_MODULE_EXPORT void on_btnabout_clicked(GtkButton *button, gpointer data)
{
    GtkWidget *dialog = gtk_dialog_new_with_buttons(
        "О программе", mainWindowObjects.main_window,
        GTK_DIALOG_MODAL | GTK_DIALOG_DESTROY_WITH_PARENT, "_OK", GTK_RESPONSE_NONE, NULL);
    GtkWidget *content_area = gtk_dialog_get_content_area(GTK_DIALOG(dialog));
    gtk_container_set_border_width(GTK_CONTAINER(content_area), 15);
    GtkWidget *label = gtk_label_new("\nРазработчик: Ярослав Онофрийчук\n");
    gtk_container_add(GTK_CONTAINER(content_area), label);
    gtk_widget_show(label);
    gtk_dialog_run(GTK_DIALOG(dialog));
    gtk_widget_destroy(dialog);
}

G_MODULE_EXPORT void on_window_destroy(GtkWidget *window, gpointer data)
{
    gtk_main_quit();
}

G_MODULE_EXPORT void on_btnexit_clicked(GtkWidget *window, gpointer data)
{
    gtk_main_quit();
}

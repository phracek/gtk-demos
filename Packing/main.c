#include <gtk/gtk.h>

/* This is a callback function. The data arguments are ignored
 * in this example. More on callbacks below.
 */
static void
print_hello (GtkWidget *widget,
             gpointer   data)
{
  g_print ("Hello World\n");
  g_print ("%s\n", data);
}

int
main (int   argc,
      char *argv[])
{
  /* GtkWidget is the storage type for widgets */
  GtkWidget *window;
  GtkWidget *button;
  GtkWidget *grid;

  /* This is called in all GTK applications. Arguments are parsed
   * from the command line and are returned to the application.
   */
  gtk_init (&argc, &argv);

  /* create a new window, and set its title */
  window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
  gtk_window_set_title (GTK_WINDOW (window), "Grid Example");
  g_signal_connect (window, "destroy", G_CALLBACK (gtk_main_quit), NULL);
  gtk_container_set_border_width(GTK_CONTAINER(window), 10);
  
  grid = gtk_grid_new();
  gtk_container_add(GTK_CONTAINER (window), grid);
  
  button = gtk_button_new_with_label("Button 1");
  g_signal_connect(button, "clicked", G_CALLBACK (print_hello), "Button 1");
  gtk_grid_attach(GTK_GRID(grid), button, 0, 0, 1, 1);
  button = gtk_button_new_with_label("Button 2");
  g_signal_connect(button, "clicked", G_CALLBACK (print_hello), "Button 2");
  gtk_grid_attach(GTK_GRID(grid), button, 1, 0, 1, 1);
  button = gtk_button_new_with_label("Quit");
  g_signal_connect(button, "clicked", G_CALLBACK (gtk_main_quit), "Quit");
  gtk_grid_attach(GTK_GRID(grid), button, 0, 1, 2, 1);
  /* ... and the window */
  gtk_widget_show_all (window);

  /* All GTK applications must have a gtk_main(). Control ends here
   * and waits for an event to occur (like a key press or a mouse event),
   * until gtk_main_quit() is called.
   */
  gtk_main ();

  return 0;
}

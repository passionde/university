#include <linux/module.h>
#include <linux/fs.h>
#include <linux/cdev.h>
#include <linux/device.h>
#include <linux/uaccess.h>
#include <linux/random.h>
#include <linux/cdev.h>
#include <linux/delay.h>
#include <linux/device.h>
#include <linux/fs.h>
#include <linux/init.h>
#include <linux/irq.h>
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/poll.h>
#include <linux/mutex.h>

#define DEVICE_NAME "password_gen"

static dev_t dev_num;
static struct cdev c_dev;
static struct class *cl;
char* charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{};:,.<>/?\0";

static int open(struct inode *inode, struct file *file) 
{
    return 0;
}

static ssize_t read(struct file *file, char __user *buf, size_t len, loff_t *off)
{
    char *temp_buf = kmalloc(1024, GFP_KERNEL);
    size_t length = 0;
    size_t charset_length = 83;
    char password[1024];
    size_t temp;
    if (copy_from_user(temp_buf, buf, len)) {
        return -EFAULT;
    }

    while( *temp_buf >= '0' && *temp_buf <= '9' ) {
        length *= 10;
        length += *temp_buf++;
        length -= '0';
    }
    temp = length;
    printk(KERN_INFO "Reading password %lu\n", length);

    while (temp)
    {
        temp--;
        get_random_bytes(&password[temp], 1);
        password[temp] = charset[password[temp] % charset_length];
    }
    password[length] = '\0';
    if (copy_to_user(buf, password, length))
        return -EFAULT;
    return length; 
}

static struct file_operations fops = {
    .owner   =  THIS_MODULE,
    .open    =  open,
    .read    =  read,
};

static int __init password_gen_init(void) 
{
    int ret;
    ret = alloc_chrdev_region(&dev_num, 0, 1, DEVICE_NAME);
    if (ret) {
        pr_err("Failed to allocate char device region\n");
        return ret;
    } 

    cdev_init(&c_dev, &fops);
    c_dev.owner = THIS_MODULE;
    ret = cdev_add(&c_dev, dev_num, 1);
    if (ret) {
        pr_err("Failed to add cdev\n");
        goto unregister;
    }

    cl = class_create(THIS_MODULE, DEVICE_NAME);
    device_create(cl, NULL, dev_num, NULL, DEVICE_NAME);

    pr_info("Password generator loaded\n");
    return 0;

unregister:
    unregister_chrdev_region(dev_num, 1);
    return ret;
}

static void __exit password_gen_exit(void) 
{
    device_destroy(cl, dev_num);
    class_destroy(cl);
    cdev_del(&c_dev);
    unregister_chrdev_region(dev_num, 1); 
    pr_info("Password generator unloaded\n");
}

module_init(password_gen_init);
module_exit(password_gen_exit);


MODULE_AUTHOR("Yarik"); 
MODULE_DESCRIPTION("Password generator device driver");

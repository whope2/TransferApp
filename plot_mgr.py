#import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') #prevent 'no display error' while plotting on AWS EC2 isntance
import matplotlib.pyplot as plt
import file_mgr

def plot(x,y):
    plot_file = "static/plot.png"

    x_list = [float(i) for i in x.split(',')]
    y_list = [float(i) for i in y.split(',')]

    plt.plot(x_list,y_list)
    plt.ylabel('Y')
    plt.xlabel('X')
    file_mgr.save_plot_data(x_list,y_list)
    plt.savefig(plot_file)
    #plt.show()
    return(plot_file)


plot("1.2,2,3,4","1.9,4,8,20")
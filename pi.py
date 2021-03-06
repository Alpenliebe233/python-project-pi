import pygal
class Pi:
    filename="pi_digits.txt"
    with open(filename) as file_object:
        contents=file_object.read()
        print(contents)
        a=[0,0,0,0,0,0,0,0,0,0]
        for i in contents:
            if i=='0':
                a[0]=a[0]+1
            elif i=='1':
                a[1]=a[1]+1
            elif i=='2':
                a[2]=a[2]+1
            elif i=='3':
                a[3]=a[3]+1
            elif i=='4':
                a[4]=a[4]+1
            elif i=='5':
                a[5]=a[5]+1
            elif i=='6':
                a[6]=a[6]+1
            elif i=='7':
                a[7]=a[7]+1
            elif i=='8':
                a[8]=a[8]+1
            elif i=='9':
                a[9]=a[9]+1
class Run:
    pi=Pi()
    result=pygal.Bar()
    result.title="The distribution of 0 to 9"
    result.x_labels=['0','1','2','3','4','5','6','7','8','9']
    result.x_title="Numbers"
    result.y_title="The number of occurrences"
    result.add("D10",pi.a)
    result.render_to_file('distribution_visual.svg')





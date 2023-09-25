def subnetmask():
    from Quizzes.Quiz_6.normal.basic import pow
    subnetmask = int(input("Please enter first octet of subnetmask number:"))
    subnetmask_2 = int(input("Please enter second octet of subnetmask number:"))
    subnetmask_3 = int(input("Please enter third octet of subnetmask number:"))
    #subnetmask_4 = int(input("Please enter fourth octet of subnetmask number:"))
    subnetmask_4=0
    if subnetmask>=128 or subnetmask==0 and subnetmask_2>=128 or subnetmask_2==0 and subnetmask_3>=128\
            or subnetmask_3==0 and subnetmask_4>=128 or subnetmask_4==0:
        print("Subnetmask ID:{}.{}.{}.{}".format(subnetmask, subnetmask_2, subnetmask_3, subnetmask_4))
        subnetmask_bits = format(subnetmask, '08b') + '.' + format(subnetmask_2, '08b') + \
                          '.' + format(subnetmask_3, '08b') + '.' + format(subnetmask_4, '08b')
        print("32 bit version:", subnetmask_bits)
        subnetmask_bits_count = subnetmask_bits.count('1')
        zero_number = 32 - subnetmask_bits_count
        print("{}.{}.{}.{}/{}".format(subnetmask, subnetmask_2, subnetmask_3, subnetmask_4, subnetmask_bits_count))
        if subnetmask != 0 and subnetmask_2 == 0 and subnetmask_3 == 0 and subnetmask_4 == 0:
            print("A class subnet mask.")
        if subnetmask != 0 and subnetmask_2 != 0 and subnetmask_3 == 0 and subnetmask_4 == 0:
            print("B class subnet mask.")
        if subnetmask != 0 and subnetmask_2 != 0 and subnetmask_3 != 0 and subnetmask_4 == 0:
            print("C class subnet mask.")
        print("Maximum number of devices that can be connected to the network=", (pow(2,zero_number)) - 2)




subnetmask()
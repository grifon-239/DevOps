


def countShell(output_file):
    file_pass = open("/etc/passwd", 'r')
    lines = []
    shells_name = ['/bin/sh', '/bin/bash', '/bin/rbash', '/bin/dash', '/bin/false']
    shells_count = {}
    for line in file_pass:
        lines.append(line[:-1].split(":"))

    for line in lines:
        if line[-1] in shells_name:
            if line[-1] in shells_count.keys():
                shells_count[line[-1]] += 1
            else:
                shells_count[line[-1]] = 1

    for key, value in shells_count.items():
        output_file.write(str(key)+" - "+str(value)+"\n")


    file_pass.close()


def userUid():
    file_pass = open("/etc/passwd", 'r')
    lines = []
    user_uid = {}
    user_uid[''] = ''
    for line in file_pass:
        lines.append(line[:-1].split(":"))

    for line in lines:
        user_uid[line[0]] = line[2]

    file_pass.close()
    return user_uid

def userUidOfGroup(user_uid, output_file):
    file_group = open('/etc/group','r')
    lines = []

    for line in file_group:
        lines.append(line[:-1].split(":"))

    for line in lines:
        line[-1] = [user_uid[i] for i in line[-1].split(",")]
        output_file.write(str(line[0]) + ": ")
        for i in line[-1]:
            output_file.write(i + " ")
        output_file.write("\n")




f = open("output.txt", "w")

countShell(f)
userUidOfGroup(userUid(), f)
f.close()

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import os
import subprocess
import shutil


def root(request):
    files = ''
    return render(request, 'intro.html', {
        'current_working_directory': os.getcwd(),
        'all_list': subprocess.check_output('dir', universal_newlines=True).split('\n')[0:-1],
        'files': files,
    })


def level_up(request):
    os.chdir('..')
    return redirect('home')


def cd(request, path):
    os.chdir(str(path))
    return redirect('home')


def md(request):
    folder_name = request.GET.get('folder_name')
    os.mkdir(str(folder_name))
    return redirect('home')


def rm(request, folder_name):
    shutil.rmtree(folder_name)
    return redirect('home')


def file_md(request, path):
    file_name = request.GET.get('file_name')
    if '.' not in file_name:
        file_name += ".txt"
    with open(os.path.join(path, file_name), 'w') as fp:
        pass
    return redirect('home')


def file_rm(request, file_name, path):
    os.chdir(path)
    os.remove(file_name)
    return redirect('home')


def file_edit(request, file_name, path):
    with open(os.path.join(path, file_name), 'r') as fp:
        file_content = fp.readlines()
    print(file_content)
    return render(request, 'fileeditor.html', {'file_content': file_content})


def dcl_check(request):
    return render(request, "index.html")

def compiler(request):
    return render(request, "run-code.html")

def run_code(request):
    code = request.GET.get('code')
    with open("codes/code.py", "w") as file:
        file.write(code)
    cmd = ['bash', 'script.sh']  
    # cmd = ["python3", "codes/code.py"]
    sp = subprocess.Popen(cmd, stdin=subprocess.PIPE, 
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            universal_newlines=True)
    try:
        sp.wait(timeout=16)
        run_output, run_error = sp.communicate()
    except subprocess.TimeoutExpired:
        sp.kill()
        run_output, run_error = sp.communicate()
    print("@@ ", run_output, "\n\n@@", run_error)
    return JsonResponse({"data": {"output": run_output, "error": run_error}})


def test_code(request):
    code = request.GET.get('code')
    with open("codes/code.py", "w") as file:
        file.write(code)
    cmd = ["pytest", "codes/test_with_pytest.py"]
    sp = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, 
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            universal_newlines=True)
    try:
        sp.wait(timeout=16)
        run_output, run_error = sp.communicate()
    except subprocess.TimeoutExpired:
        sp.kill()
        run_output, run_error = sp.communicate()
    print("@@ ", run_output, "\n\n@@", run_error)
    return JsonResponse({"data": {"output": run_output, "error": run_error}})




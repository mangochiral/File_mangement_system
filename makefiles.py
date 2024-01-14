import os

class foldersandfiles:

  def __init__(self):
    self.folder = {}
#The block below make folders and files inside them
  def add_folder(self, folder, file):
    tmp = []
    for i in range(file):
      filename = "file_" + str(i) + ".txt"
      # for custom file name for use below variable
      # filename = input("Enter file name: ") + input("Enter file extension: ")
      tmp.append(filename)
    self.folder.update({folder: tmp})
    # print(self.folder)
    for i in self.folder:
      if (not os.path.exists(i)):
        os.mkdir(i)
      os.chdir(i + '/')
      for j in self.folder[i]:
        with open(j, 'w') as f:
          f.write(f"Write your text here!")
      os.chdir("..")

  # def print_folders(self):
  #   print(f"{self.folder}")


a = foldersandfiles()
a.add_folder(input("Enter folder name: "), int(input("Enter number of files: ")))
a.add_folder(input("Enter folder name: "), int(input("Enter number of files: ")))

x={}
print(type(x))

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23} #Mixed up both data types
print(file_counts)

print(file_counts["txt"])

print("jpg" in file_counts)

print("html" in file_counts)

file_counts ["cfg"] = 8
print(file_counts)          #immutable

file_counts ["csv"] = 18
print(file_counts)          #replaced

del file_counts ["cfg"]
print(file_counts)          #delete

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:                           #for
    print(extension)

for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, ext))

print(file_counts.keys())

print(file_counts.values())

for value in file_counts.values():
    print(value)

#--------------------------------------------------------------------------------------

def check_guests(guest_list, guest):
  return guest_list[guest] # Return the value for the given key


guest_list = { "Adam":3, "Camila":3, "David":5, "Jamal":3, "Charley":2, "Titus":1, "Raj":6, "Noemi":1, "Sakira":3, "Chidi":5}


print(check_guests(guest_list, "Adam")) # Should print 3
print(check_guests(guest_list, "Sakira")) # Should print 3
print(check_guests(guest_list, "Charley")) # Should print 2
                
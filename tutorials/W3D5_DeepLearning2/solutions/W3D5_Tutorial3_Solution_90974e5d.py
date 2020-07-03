
missing_a = 1
missing_b = 0

my_input_train = input_train[(y_train!=missing_a)&(y_train!=missing_b)]
my_input_test = input_test[(y_test!=missing_a)&(y_test!=missing_b)]
my_y_test = y_test[(y_test!=missing_a)&(y_test!=missing_b)]

print(my_input_train.shape)
print(my_input_test.shape)
print(my_y_test.shape)
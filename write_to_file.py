f = open('implementation/libgdx_test_shuffled_output.json', "rb")

out = open('implementation/libgdx_output_small.json', "w+")

out.write(f.read(1024*16))


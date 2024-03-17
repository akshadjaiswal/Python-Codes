def main():
    with open("./Images/React.jpg","rb") as existing_image, open("xyz.jpg","wb") as new_image:
        for each_line_bytes in existing_image:
            new_image.write(each_line_bytes)
            
if __name__ == "__main__":
    main()
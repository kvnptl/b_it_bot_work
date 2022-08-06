
'''

Split the dataset into train, test and validation sets.

The code will create a folder for each set and copy the files into it.

Author: Kevin Patel
Date:   2022-07-17

'''

from sklearn.model_selection import train_test_split
import splitfolders
import glob as glob
import random
import os

'''

input:
    - path: 
        path to the images files
        path to the labels files

output:
    - train, test, validation folders created in the same directory as the input

'''


def split_dataset(input_image_folder, input_label_folder, train_percentage, test_percentage, validation_percentage):

    # check if the folders exist
    if not os.path.exists(input_image_folder):
        print('\u274C' + 'The input image folder does not exist')
        return False
    if not os.path.exists(input_label_folder):
        print('\u274C' + 'The input label folder does not exist')
        return False

    # list of all the files in the input_image_folder and input_label_folder
    images = os.listdir(input_image_folder)
    labels = os.listdir(input_label_folder)

    # sort the images and labels by name
    images.sort()
    labels.sort()

    # check if the number of images and labels match
    if len(images) != len(labels):
        print('\u274C' + 'The number of images and labels does not match')
        return False

    # split data and labels into train and test
    x_train, x_test, y_train, y_test = train_test_split(
        images, labels, test_size=test_percentage, random_state=230)

    # divide train into train and validation
    x_train, x_valid, y_train, y_valid = train_test_split(
        x_train, y_train, test_size=validation_percentage, random_state=230)

    # print the sizes of the train, validation, and test sets
    print('Train set: ', len(x_train))
    print('Validation set: ', len(x_valid))
    print('Test set: ', len(x_test))

    # extract folder names from the paths
    train_image_folder = os.path.basename(input_image_folder)
    train_label_folder = os.path.basename(input_label_folder)

    # create a new folder for the train, validation and test data
    output_train_folder = input_image_folder.replace(
        train_image_folder, 'train/images')
    output_valid_folder = input_image_folder.replace(
        train_image_folder, 'valid/images')
    output_test_folder = input_image_folder.replace(
        train_image_folder, 'test/images')
    output_train_label_folder = input_label_folder.replace(
        train_label_folder, 'train/labels')
    output_valid_label_folder = input_label_folder.replace(
        train_label_folder, 'valid/labels')
    output_test_label_folder = input_label_folder.replace(
        train_label_folder, 'test/labels')

    # check if the folders exist, if not create them
    if not os.path.exists(output_train_folder):
        os.makedirs(output_train_folder)

        # copy the images to the train folder
        for image in x_train:
            src = os.path.join(input_image_folder, image)
            dst = os.path.join(output_train_folder, image)
            os.system('cp ' + src + ' ' + dst)

    if not os.path.exists(output_valid_folder):
        os.makedirs(output_valid_folder)

        # copy the images to the validation folder
        for image in x_valid:
            src = os.path.join(input_image_folder, image)
            dst = os.path.join(output_valid_folder, image)
            os.system('cp ' + src + ' ' + dst)

    if not os.path.exists(output_test_folder):
        os.makedirs(output_test_folder)

        # copy the images to the test folder
        for image in x_test:
            src = os.path.join(input_image_folder, image)
            dst = os.path.join(output_test_folder, image)
            os.system('cp ' + src + ' ' + dst)

    if not os.path.exists(output_train_label_folder):
        os.makedirs(output_train_label_folder)

        # copy the labels to the train folder
        for label in y_train:
            src = os.path.join(input_label_folder, label)
            dst = os.path.join(output_train_label_folder, label)
            os.system('cp ' + src + ' ' + dst)

    if not os.path.exists(output_valid_label_folder):
        os.makedirs(output_valid_label_folder)

        # copy the labels to the validation folder
        for label in y_valid:
            src = os.path.join(input_label_folder, label)
            dst = os.path.join(output_valid_label_folder, label)
            os.system('cp ' + src + ' ' + dst)

    if not os.path.exists(output_test_label_folder):
        os.makedirs(output_test_label_folder)

        # copy the labels to the test folder
        for label in y_test:
            src = os.path.join(input_label_folder, label)
            dst = os.path.join(output_test_label_folder, label)
            os.system('cp ' + src + ' ' + dst)

    # sanity check
    # if number of files in output_train_folder is not equal to the number of files in x_train, then something went wrong
    if len(os.listdir(output_train_folder)) == len(x_train):
        if len(os.listdir(output_valid_folder)) == len(x_valid):
            if len(os.listdir(output_test_folder)) == len(x_test):
                if len(os.listdir(output_train_label_folder)) == len(y_train):
                    if len(os.listdir(output_valid_label_folder)) == len(y_valid):
                        if len(os.listdir(output_test_label_folder)) == len(y_test):
                            print('Dataset split completed successfully' + ' \u2705')
                        else:
                            print('Error: Something went wrong' + ' \u274C')
                    else:
                        print('Error: Something went wrong' + ' \u274C')
                else:
                    print('Error: Something went wrong' + ' \u274C')
            else:
                print('Error: Something went wrong' + ' \u274C')

    return True


def main():

    #########
    # INPUT #

    # The path to the directory where the original dataset is stored
    input_image_folder = 'b_it_bot_dataset/atwork_realdata_combined/training_copy_4/image'
    input_label_folder = 'b_it_bot_dataset/atwork_realdata_combined/training_copy_4/labels_yolo'

    # define percentage of train, test and validation sets
    train_percentage = 0.85
    test_percentage = 0.05
    validation_percentage = 0.10

    #########

    out = split_dataset(input_image_folder, input_label_folder,
                        train_percentage, test_percentage, validation_percentage)

    if not out:
        raise Exception('Error: Something went wrong')


if __name__ == "__main__":
    main()

import sys
import cv2


def load_image():
    """Loads an image from disk, returns it as a single instance"""
    return cv2.imread('test.png')
    pass


def show_image(image):
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass


def pixelate_image(image):
    """ Apply a pixelating filter to the image """

    height, width = image.shape[:2]  # We know it should be a fixed res
    blurred_image = cv2.medianBlur(image, 61)


    """ 16:9 aspect ratio means we can make (16:9) * n size blocks """
    width_increment = 16
    height_increment = 9

    # Init matrix
    roi_matrix = [[0 for x in range(width / width_increment)] for y in range(height / height_increment)]

    # Fill matrix with ROIs
    for x in range(0, width-width_increment, width_increment):
        for y in range(0, height - height_increment, height_increment):
            roi_matrix[x/width_increment][y/height_increment] = blurred_image[int(y):int(y + height_increment), int(x):int(x + width_increment)]

    im_crop = roi_matrix[2][1]

    show_image(im_crop)

    # Debug only
    for i in range(0, width, width_increment):
        cv2.line(blurred_image, pt1=(i, 0), pt2=(i, height), color=(0, 0, 0), thickness=1)

    for i in range(0, height, height_increment):
        cv2.line(blurred_image, pt1=(0, i), pt2=(width, i), color=(0, 0, 0), thickness=1)

    show_image(blurred_image)

    return roi_matrix
    pass


def create_sound_map():
    """Create a matrix the size of the large pixels and place on each position
     a corresponding value for frequency and phase"""
    pass


def process_sound_map():
    """Create a single sound characteristic (a vector of amplitude values) based on the map"""
    pass


def play_sound():
    pass


def normalize_image(image):
    """ Resize to 720p """
    return cv2.resize(image, (1280, 720), interpolation=cv2.INTER_CUBIC)
    pass


def main():
    """Main entry point for the script."""
    test_image = load_image()

    pixelate_image(
        normalize_image(test_image)
    )
    pass

if __name__ == '__main__':
    sys.exit(main())

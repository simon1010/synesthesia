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
    """Apply a pixelating filter to the image"""
    return cv2.medianBlur(image, 31)
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


def main():
    """Main entry point for the script."""

    test_image = load_image()
    show_image(pixelate_image(test_image))
    pass

if __name__ == '__main__':
    sys.exit(main())

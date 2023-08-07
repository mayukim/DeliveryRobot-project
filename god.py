import customtkinter
import cv2
from PIL import Image,ImageTk
import rospy
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge

class ImageCanvas(customtkinter.CTkCanvas):
    def __init__(self, master, canvas_width, canvas_height):
        super().__init__(master=master, width=canvas_width, height=canvas_height, bg="black")

    def update_canvas(self, ros_image):
        # Convert ROS compressed image to OpenCV format
        bridge = CvBridge()
        cv_image = bridge.compressed_imgmsg_to_cv2(ros_image)

        # Convert BGR to RGB
        cv_image_rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        cv_image_rgb = cv2.resize(cv_image_rgb, (1000, 600))

        # Convert to PhotoImage format
        pil_image = Image.fromarray(cv_image_rgb)
        photo = ImageTk.PhotoImage(image=pil_image)

        # Update the canvas with the new image
        self.create_image(0, 0, anchor="nw", image=photo)
        self.image = photo  # Keep a reference to prevent the image from being garbage collected

class Create_Frame(customtkinter.CTkFrame):
    def __init__(self, master, padx, pady):
        super().__init__(master=master)
        self.pack(pady=pady, padx=padx, fill="both", expand=True)

class Button_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class DeliveryRobotApp(customtkinter.CTk):
    def __init__(self, geometry, title):
        super().__init__()

        self.map_img = self.image_create('../../../../Downloads/scripts/map.png')
        self.status_img = self.image_create('../../../../Downloads/scripts/vote.png')
        self.camera_img = self.image_create('../../../../Downloads/scripts/video.png')
        self.stop_img = self.image_create('../../../../Downloads/scripts/stop.png')

        self.geometry(geometry)
        self.title(title)

        self.main_frame = Create_Frame(self, 200, 50)

        self.camera_frame = Create_Frame(self.main_frame, 0, 0)
        self.image_canvas = ImageCanvas(self.camera_frame, canvas_width=640, canvas_height=480)
        self.image_canvas.pack(fill="both", expand=True)

        self.buttons_frame = Create_Frame(self,0,0)

        # Create a list of five buttons and pack them inside the buttons frame
        self.buttons_list = ['Show map','Show camera','Show status','Stop']
        self.image_list = [self.map_img,self.camera_img,self.status_img,self.stop_img]
        self.command_list = [self.Show_map,self.Show_camera,self.Show_status,self.Stop]
        for i,data in enumerate(self.buttons_list) :
            button = customtkinter.CTkButton(self.buttons_frame, text=data,height=70,image=self.image_list[i],fg_color="white",text_color="black",command=self.command_list[i])
            button.grid(row=0, column=i, padx=100, pady=20)


        # Initialize ROS node
        rospy.init_node("delivery_robot_app", anonymous=True)

        # Subscribe to the /skeleton_img topic
        rospy.Subscriber("/camera/rgb/image_raw/compressed", CompressedImage, self.image_callback)

    def image_callback(self, ros_image):
        # Update the canvas with the received ROS compressed image
        self.image_canvas.update_canvas(ros_image)
    def image_create(self,path):
        my_image = customtkinter.CTkImage(light_image=Image.open(path),size=(50,50))
        return my_image
    def Show_map(self):
        pass
    def Show_camera(self):
        pass
    def Show_status(self):
        pass
    def Stop(self):
        pass

if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app = DeliveryRobotApp("1400x700", "배송로봇")
    app.mainloop()
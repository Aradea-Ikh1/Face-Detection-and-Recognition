import customtkinter
import cv2
import face_recognition as FR
font = cv2.FONT_HERSHEY_PLAIN
import os
import numpy as np
from tkinter import simpledialog
from tkinter import filedialog
from PIL import Image

# Mengatur mode tampilan dan tema untuk customtkinter
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

# Mendefinisikan kelas utama untuk aplikasi
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Konfigurasi jendela utama
        self.title("Face Detection and Recognition System")
        self.geometry(f"{1280}x{720}")
        self.resizable(width=False, height=False)

        # Konfigurasi layout grid (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Membuat frame sidebar dengan widget
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=3, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        # Label logo di sidebar
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame,
                                                 text="Main Menu",
                                                 font=customtkinter.CTkFont("Poppins", 20, "bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Tombol di sidebar
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,
                                                        text="Home Page",
                                                        font=customtkinter.CTkFont("Poppins", 12, "bold"),
                                                        command=self.sidebar_home_event,
                                                        text_color="white")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,
                                                        text="Fundamental",
                                                        font=customtkinter.CTkFont("Poppins", 12, "bold"),
                                                        command=self.sidebar_fundamental_event,
                                                        text_color="white")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,
                                                        text="Simulation",
                                                        font=customtkinter.CTkFont("Poppins", 12, "bold"),
                                                        command=self.sidebar_simulation_event,
                                                        text_color="white")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame,
                                                        text="Tutorial",
                                                        font=customtkinter.CTkFont("Poppins", 12, "bold"),
                                                        command=self.sidebar_tutorial_event,
                                                        text_color="white")
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)

        # Label mode tampilan di sidebar
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame,
                                                            text="Display Mode:",
                                                            font=customtkinter.CTkFont("Poppins", 12, "bold"),
                                                            anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))

        # Menu pilihan mode tampilan
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       font = customtkinter.CTkFont("Poppins", 12, "bold"),
                                                                       command=self.change_appearance_mode_event,
                                                                       text_color="white")
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 10))

        # Label versi awal di sidebar
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame,
                                                    text="Early Ver.",
                                                    font=customtkinter.CTkFont("Helvetica", 12, "bold"),
                                                    anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(10, 20))

        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.sidebar_home_event() # Menampilkan halaman utama

    # Fungsi untuk mengubah mode tampilan
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # Fungsi untuk menampilkan halaman utama
    def sidebar_home_event(self):
        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=1, rowspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.tabview.add("Home Page")

        # Menambahkan label untuk halaman utama dengan teks centered
        home_text = "PENGOLAHAN SINYAL DAN LAYANAN MULTIMEDIA\nFACE DETECTION AND RECOGNITION"
        self.home_label = customtkinter.CTkLabel(self.tabview.tab("Home Page"),
                                                 text=home_text,
                                                 font=customtkinter.CTkFont("Poppins", 29, "bold"),
                                                 anchor="center")
        self.home_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")

        # Menambahkan gambar
        my_image = customtkinter.CTkImage(light_image=Image.open("recog_home.jpg"),
                                          dark_image=Image.open("recog_home.jpg"),
                                          size=(480, 270))
        self.image_label = customtkinter.CTkLabel(self.tabview.tab("Home Page"),
                                                  image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")

        # Menambahkan label untuk informasi kelompok dengan teks centered
        group_info = "KELOMPOK 10\n2106728635 - Niken Rachmawati Suryantoro\n2106636880 - Aradea Haikal Ikhwan"
        self.group_label = customtkinter.CTkLabel(self.tabview.tab("Home Page"),
                                                  text=group_info,
                                                  font=customtkinter.CTkFont("Poppins", 24),
                                                  anchor="center")
        self.group_label.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="nsew")

        # Konfigurasi kolom dan baris grid untuk memperluas dan centered
        self.tabview.tab("Home Page").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Home Page").grid_rowconfigure(0, weight=0)

    # Fungsi untuk menampilkan tab fundamental
    def sidebar_fundamental_event(self):
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=1, rowspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.tabview.add("Introduction")

        # Label Pendahuluan
        generalintro_text = "Pendahuluan"
        self.generalintro_label = customtkinter.CTkLabel(self.tabview.tab("Introduction"),
                                                    text=generalintro_text,
                                                    font=customtkinter.CTkFont("Poppins", 16, "bold"),
                                                    anchor="w",
                                                    justify="left")
        self.generalintro_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")

        # Label teks pendahuluan
        generalintro1_text = "Program ini merupakan sistem deteksi dan pengenalan wajah berbasis antarmuka pengguna grafis (GUI) yang dibangun menggunakan beberapa pustaka Python utama. Antarmuka pengguna dikembangkan dengan customtkinter, sementara fungsi deteksi dan pengenalan wajah memanfaatkan pustaka OpenCV dan face_recognition. Sistem ini dirancang untuk memudahkan pengguna dalam melakukan deteksi dan pengenalan wajah melalui penggunaan kamera komputer (webcam)."
        self.generalintro1_label = customtkinter.CTkLabel(self.tabview.tab("Introduction"),
                                                     text=generalintro1_text,
                                                     font=customtkinter.CTkFont("Poppins", 14, "normal"),
                                                     anchor="w",
                                                     justify="left",
                                                     wraplength=950)
        self.generalintro1_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")

        # Label Tujuan
        generalintro2_text = "Tujuan"
        self.generalintro2_label = customtkinter.CTkLabel(self.tabview.tab("Introduction"),
                                                         text=generalintro2_text,
                                                         font=customtkinter.CTkFont("Poppins", 16, "bold"),
                                                         anchor="w",
                                                         justify="left")
        self.generalintro2_label.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="nsew")

        # Label teks Tujuan
        generalintro3_text = "Tujuan utama dari program ini adalah untuk menyediakan alat yang intuitif dan mudah digunakan untuk mendeteksi dan mengenali wajah. Ini bisa digunakan dalam berbagai aplikasi, seperti keamanan, absensi otomatis, atau bahkan dalam proyek penelitian yang membutuhkan identifikasi wajah secara otomatis."
        self.generalintro3_label = customtkinter.CTkLabel(self.tabview.tab("Introduction"),
                                                          text=generalintro3_text,
                                                          font=customtkinter.CTkFont("Poppins", 14, "normal"),
                                                          anchor="w",
                                                          justify="left",
                                                          wraplength=950)
        self.generalintro3_label.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="nsew")

        self.tabview.add("Library GUI")
        general_text = "GUI Libraries"
        self.general_label = customtkinter.CTkLabel(self.tabview.tab("Library GUI"),
                                                    text=general_text,
                                                    font=customtkinter.CTkFont("Poppins", 16, "bold"),
                                                    anchor="w",
                                                    justify="left")
        self.general_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")

        general1_text = "A. CustomTkinter: \ncustomtkinter merupakan library yang memperluas fungsi dari tkinter dengan menambahkan gaya modern dan tema untuk pembuatan GUI. Library ini memungkinkan pengguna untuk membuat aplikasi dengan tampilan yang lebih menarik dibandingkan dengan tkinter standar.\nFungsi dalam Program:\n- cv2.VideoCapture digunakan untuk menangkap video dari kamera.\n- cv2.namedWindow dan cv2.imshow digunakan untuk membuat jendela dan menampilkan gambar atau video.\n- cv2.waitKey digunakan untuk menangani input dari keyboard.\n- cv2.imwrite digunakan untuk menyimpan gambar yang diambil dari kamera.\n- cv2.rectangle dan cv2.putText digunakan untuk menggambar persegi panjang dan menampilkan teks pada gambar."
        self.general1_label = customtkinter.CTkLabel(self.tabview.tab("Library GUI"),
                                                     text=general1_text,
                                                     font=customtkinter.CTkFont("Poppins", 14, "normal"),
                                                     anchor="w",
                                                     justify="left",
                                                     wraplength=1000)
        self.general1_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")

        general2_text = "B. PIL (Python Imaging Library): \nPIL adalah library untuk membuka, memanipulasi, dan menyimpan berbagai format gambar. PIL kini digantikan oleh Pillow, yang merupakan fork dari PIL.\nFungsi dalam Program:\n- Image.open digunakan untuk membuka gambar yang akan ditampilkan pada interface pengguna.\n- customtkinter.CTkImage digunakan untuk membuat objek gambar yang kompatibel dengan customtkinter dan menampilkan di GUI."
        self.general2_label = customtkinter.CTkLabel(self.tabview.tab("Library GUI"),
                                                     text=general2_text,
                                                     font=customtkinter.CTkFont("Poppins", 14, "normal"),
                                                     anchor="w",
                                                     justify="left",
                                                     wraplength=1000)
        self.general2_label.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="nsew")

        self.tabview.add("Library Face Recognition")
        generalfr_text = "Face Recognition Libraries"
        self.generalfr_label = customtkinter.CTkLabel(self.tabview.tab("Library Face Recognition"),
                                                    text=generalfr_text,
                                                    font=customtkinter.CTkFont("Poppins", 16, "bold"),
                                                    anchor="w",
                                                    justify="left")
        self.generalfr_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")

        generalfr1_text = "A. OpenCV (Open Source Computer Vision Library): \nOpenCV adalah library open-source yang dikembangkan untuk komputer vision. Library ini berisi ratusan fungsi untuk pengolahan gambar dan video.\nFungsi dalam Program:\n- cv2.VideoCapture digunakan untuk menangkap video dari kamera.\n- cv2.namedWindow dan cv2.imshow digunakan untuk membuat jendela dan menampilkan gambar atau video.\n- cv2.waitKey digunakan untuk menangani input dari keyboard.\n- v2.imwrite digunakan untuk menyimpan gambar yang diambil dari kamera.\n- cv2.rectangle dan cv2.putText digunakan untuk menggambar persegi panjang dan menampilkan teks pada gambar."
        self.generalfr1_label = customtkinter.CTkLabel(self.tabview.tab("Library Face Recognition"),
                                                       text=generalfr1_text,
                                                       font=customtkinter.CTkFont("Poppins", 14, "normal"),
                                                       anchor="w",
                                                       justify="left",
                                                       wraplength=1000)
        self.generalfr1_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")

        generalfr2_text = "B. Face Recognition: \nface_recognition merupakan library berbasis dlib yang cukup akurat untuk pengenalan wajah. Library ini menyediakan fungsi untuk menemukan lokasi wajah, mengenali wajah, dan mencocokkan wajah berbasis data.\nFungsi dalam Program:\n- FR.face_locations digunakan untuk mendeteksi lokasi wajah dalam gambar.\n- FR.face_encodings digunakan untuk mendapatkan encoding fitur wajah yang bisa dibandingkan satu sama lain.\n- FR.compare_faces digunakan untuk membandingkan wajah baru dengan wajah yang sudah dikenal untuk melihat apakah ada kecocokan.\n- FR.face_distance digunakan untuk menghitung jarak antara encoding wajah baru dan encoding wajah yang sudah dikenal, untuk menentukan kemiripan."
        self.generalfr2_label = customtkinter.CTkLabel(self.tabview.tab("Library Face Recognition"),
                                                       text=generalfr2_text,
                                                       font=customtkinter.CTkFont("Poppins", 14, "normal"),
                                                       anchor="w",
                                                       justify="left",
                                                       wraplength=1000)
        self.generalfr2_label.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="nsew")

        # Konfigurasi kolom dan baris grid untuk memperluas dan centered
        self.tabview.tab("Introduction").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Library GUI").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Library Face Recognition").grid_columnconfigure(0, weight=1)

    # Fungsi untuk menampilkan tab simulasi
    def sidebar_simulation_event(self):
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=1, rowspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.tabview.add("Simulation")
        # Add label indicating to Upload Image
        self.upload_label = customtkinter.CTkLabel(self.tabview.tab("Simulation"),
                                                   text="Collect Your Face Image",
                                                   font=customtkinter.CTkFont("Poppins", 14, "normal"),
                                                   anchor="w")
        self.upload_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        # Add button to upload
        self.upload_button = customtkinter.CTkButton(self.tabview.tab("Simulation"),
                                                     text="Open WebCam",
                                                     font=customtkinter.CTkFont("Poppins", 14, "normal"),
                                                     command=self.upload_event,
                                                     text_color="white")
        self.upload_button.grid(row=0, column=1, padx=20, pady=(20, 10))

        # Add label indicating to Upload Image
        self.uploadim_label = customtkinter.CTkLabel(self.tabview.tab("Simulation"),
                                                     text="Upload Face Image",
                                                     font=customtkinter.CTkFont("Poppins", 14, "normal"),
                                                     anchor="w")
        self.uploadim_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")
        # Add button to upload
        self.uploadim_button = customtkinter.CTkButton(self.tabview.tab("Simulation"),
                                                       text="Upload File",
                                                       font=customtkinter.CTkFont("Poppins", 14, "normal"),
                                                       command=self.upload_image,
                                                       text_color="white")
        self.uploadim_button.grid(row=1, column=1, padx=20, pady=(20, 10))

        # Add label indicating to open PC webcam
        self.webcam_label = customtkinter.CTkLabel(self.tabview.tab("Simulation"),
                                                   text="Face Recognizer",
                                                   font=customtkinter.CTkFont("Poppins", 14, "normal"),
                                                   anchor="w")
        self.webcam_label.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="w")
        # Add button to Simulation tab
        self.simulation_button = customtkinter.CTkButton(self.tabview.tab("Simulation"),
                                                         text="Open WebCam",
                                                         font=customtkinter.CTkFont("Poppins", 14, "normal"),
                                                         command=self.run_simulation_event,
                                                         text_color="white")
        self.simulation_button.grid(row=2, column=1, padx=20, pady=(20, 10))

    # Simulasi Tutorial
    def sidebar_tutorial_event(self):
        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=1, rowspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.tabview.add("Step 1")
        generaltutor_text = "Langkah 1 - Klik Menu Simulation"
        self.generaltutor_label = customtkinter.CTkLabel(self.tabview.tab("Step 1"),
                                                    text=generaltutor_text,
                                                    font=customtkinter.CTkFont("Poppins", 16, "bold"),
                                                    anchor="w",
                                                    justify="left")
        self.generaltutor_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
        # image tutorial step 1
        my_image = customtkinter.CTkImage(light_image=Image.open("1.png"),
                                          dark_image=Image.open("1.png"),
                                          size=(835, 470))
        self.image_label = customtkinter.CTkLabel(self.tabview.tab("Step 1"),
                                                  image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")

        self.tabview.add("Step 2")
        generaltutor1_text = "Langkah 2 - Klik Button Open WebCam pada Bagian Collect Your Face Image"
        self.generaltutor1_label = customtkinter.CTkLabel(self.tabview.tab("Step 2"),
                                                         text=generaltutor1_text,
                                                         font=customtkinter.CTkFont("Poppins", 16, "bold"),
                                                         anchor="w",
                                                         justify="left")
        self.generaltutor1_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
        # image tutorial step 2
        my_image = customtkinter.CTkImage(light_image=Image.open("2.png"),
                                          dark_image=Image.open("2.png"),
                                          size=(835, 470))
        self.image_label = customtkinter.CTkLabel(self.tabview.tab("Step 2"),
                                                  image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")

        self.tabview.add("Step 3")
        generaltutor2_text = "Langkah 3 - Akan Muncul Pop Up Window Capture Image"
        self.generaltutor2_label = customtkinter.CTkLabel(self.tabview.tab("Step 3"),
                                                          text=generaltutor2_text,
                                                          font=customtkinter.CTkFont("Poppins", 16, "bold"),
                                                          anchor="w",
                                                          justify="left")
        self.generaltutor2_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
        # image tutorial step 3
        my_image = customtkinter.CTkImage(light_image=Image.open("3.png"),
                                          dark_image=Image.open("3.png"),
                                          size=(835, 470))
        self.image_label = customtkinter.CTkLabel(self.tabview.tab("Step 3"),
                                                  image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")

        self.tabview.add("Step 4")
        generaltutor3_text = "Langkah 4 - Klik Tombol Spasi Pada Keyboard Untuk Menggambil Gambar"
        self.generaltutor3_label = customtkinter.CTkLabel(self.tabview.tab("Step 4"),
                                                          text=generaltutor3_text,
                                                          font=customtkinter.CTkFont("Poppins", 16, "bold"),
                                                          anchor="w",
                                                          justify="left")
        self.generaltutor3_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
        # image tutorial step 4
        my_image = customtkinter.CTkImage(light_image=Image.open("4.png"),
                                          dark_image=Image.open("4.png"),
                                          size=(835, 470))
        self.image_label = customtkinter.CTkLabel(self.tabview.tab("Step 4"),
                                                  image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")

        self.tabview.add("Step 5")
        generaltutor4_text = "Langkah 5 - Akan Muncul Pop Up Window Enter Your Name, Ketik Nama Pemilik Wajah!"
        self.generaltutor4_label = customtkinter.CTkLabel(self.tabview.tab("Step 5"),
                                                          text=generaltutor4_text,
                                                          font=customtkinter.CTkFont("Poppins", 16, "bold"),
                                                          anchor="w",
                                                          justify="left")
        self.generaltutor4_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
        # image tutorial step 5
        my_image = customtkinter.CTkImage(light_image=Image.open("5.png"),
                                          dark_image=Image.open("5.png"),
                                          size=(835, 470))
        self.image_label = customtkinter.CTkLabel(self.tabview.tab("Step 5"),
                                                  image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")

        self.tabview.add("Step 6")
        generaltutor5_text = "Langkah 6 - Klik Button Open WebCam pada Bagian Face Recognizer"
        self.generaltutor5_label = customtkinter.CTkLabel(self.tabview.tab("Step 6"),
                                                          text=generaltutor5_text,
                                                          font=customtkinter.CTkFont("Poppins", 16, "bold"),
                                                          anchor="w",
                                                          justify="left")
        self.generaltutor5_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
        # image tutorial step 6
        my_image = customtkinter.CTkImage(light_image=Image.open("6.png"),
                                          dark_image=Image.open("6.png"),
                                          size=(835, 470))
        self.image_label = customtkinter.CTkLabel(self.tabview.tab("Step 6"),
                                                  image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")

        self.tabview.add("Step 7")
        generaltutor6_text = "Langkah 7 - Akan Muncul Pop Up Window My Face, Wajah Akan Terdeteksi Beserta Nama Yang Sesuai Dengan Data Yang Ada"
        self.generaltutor6_label = customtkinter.CTkLabel(self.tabview.tab("Step 7"),
                                                          text=generaltutor6_text,
                                                          font=customtkinter.CTkFont("Poppins", 16, "bold"),
                                                          anchor="w",
                                                          justify="left",
                                                          wraplength=1000)
        self.generaltutor6_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
        # image tutorial step 7
        my_image = customtkinter.CTkImage(light_image=Image.open("7.png"),
                                          dark_image=Image.open("7.png"),
                                          size=(835, 470))
        self.image_label = customtkinter.CTkLabel(self.tabview.tab("Step 7"),
                                                  image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")

        self.tabview.add("Step 8")
        generaltutor7_text = "Langkah 8 - Klik Tombol Q Pada Keyboard Untuk Menutup Pop Up Window My Face"
        self.generaltutor7_label = customtkinter.CTkLabel(self.tabview.tab("Step 8"),
                                                          text=generaltutor7_text,
                                                          font=customtkinter.CTkFont("Poppins", 16, "bold"),
                                                          anchor="w",
                                                          justify="left")
        self.generaltutor7_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
        # image tutorial step 8
        my_image = customtkinter.CTkImage(light_image=Image.open("8.png"),
                                          dark_image=Image.open("8.png"),
                                          size=(835, 470))
        self.image_label = customtkinter.CTkLabel(self.tabview.tab("Step 8"),
                                                  image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")

        self.tabview.add("Step 9")
        generaltutor9_text = "Langkah 9 - Klik Tombol Q Pada Keyboard Untuk Menutup Pop Up Window My Face"
        self.generaltutor9_label = customtkinter.CTkLabel(self.tabview.tab("Step 9"),
                                                          text=generaltutor9_text,
                                                          font=customtkinter.CTkFont("Poppins", 16, "bold"),
                                                          anchor="w",
                                                          justify="left")
        self.generaltutor9_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
        # image tutorial step 9
        my_image = customtkinter.CTkImage(light_image=Image.open("9.png"),
                                          dark_image=Image.open("9.png"),
                                          size=(835, 470))
        self.image_label = customtkinter.CTkLabel(self.tabview.tab("Step 9"),
                                                  image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")

        self.tabview.add("Step 10")
        generaltutor10_text = "Langkah 10 - Muncul Pop-Up Window dan Pilih File Yang Ingin di Upload"
        self.generaltutor10_label = customtkinter.CTkLabel(self.tabview.tab("Step 10"),
                                                          text=generaltutor10_text,
                                                          font=customtkinter.CTkFont("Poppins", 16, "bold"),
                                                          anchor="w",
                                                          justify="left")
        self.generaltutor10_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
        # image tutorial step 10
        my_image = customtkinter.CTkImage(light_image=Image.open("10.png"),
                                          dark_image=Image.open("10.png"),
                                          size=(835, 470))
        self.image_label = customtkinter.CTkLabel(self.tabview.tab("Step 10"),
                                                  image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")

        self.tabview.add("Step 11")
        generaltutor11_text = "Langkah 11 - Klik Kanan Mouse Pada File dan Rename File Menjadi Nama Pemilik Wajah"
        self.generaltutor11_label = customtkinter.CTkLabel(self.tabview.tab("Step 11"),
                                                          text=generaltutor11_text,
                                                          font=customtkinter.CTkFont("Poppins", 16, "bold"),
                                                          anchor="w",
                                                          justify="left")
        self.generaltutor11_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
        # image tutorial step 11
        my_image = customtkinter.CTkImage(light_image=Image.open("11.png"),
                                          dark_image=Image.open("11.png"),
                                          size=(835, 470))
        self.image_label = customtkinter.CTkLabel(self.tabview.tab("Step 11"),
                                                  image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")

        self.tabview.add("Step 12")
        generaltutor12_text = "Langkah 12 - Setelah Klik Open, File Yang Sudah di Pilih Akan Masuk Ke Directory Database"
        self.generaltutor12_label = customtkinter.CTkLabel(self.tabview.tab("Step 12"),
                                                          text=generaltutor12_text,
                                                          font=customtkinter.CTkFont("Poppins", 16, "bold"),
                                                          anchor="w",
                                                          justify="left")
        self.generaltutor12_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
        # image tutorial step 12
        my_image = customtkinter.CTkImage(light_image=Image.open("12.png"),
                                          dark_image=Image.open("12.png"),
                                          size=(835, 470))
        self.image_label = customtkinter.CTkLabel(self.tabview.tab("Step 12"),
                                                  image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="nsew")

        # Configure grid columns and rows to expand and center
        self.tabview.tab("Step 1").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Step 2").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Step 3").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Step 4").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Step 5").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Step 6").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Step 7").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Step 8").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Step 9").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Step 10").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Step 11").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Step 12").grid_columnconfigure(0, weight=1)

    # Function to handle capture image
    def upload_event(self):
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("Capture Image")

        while True:
            ret, frame = cam.read()
            if not ret:
                print("Failed to grab frame")
                break
            cv2.imshow("Capture Image", frame)

            k = cv2.waitKey(1)
            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k % 256 == 32:
                # SPACE pressed
                name = simpledialog.askstring("Input", "Enter your name:")
                if name:
                    img_name = f"FaceList\{name}.jpg"
                    cv2.imwrite(img_name, frame)
                    print(f"{img_name} saved!")
                break

        cam.release()
        cv2.destroyAllWindows()

    def upload_image(self):
        # Function to handle image upload
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            try:
                # Save the uploaded image to the specified directory
                save_path = os.path.join("FaceList", os.path.basename(file_path))
                image = Image.open(file_path)
                image.save(save_path)
                customtkinter.CTkMessagebox.show_info("Success", f"Image uploaded and saved to {save_path}")
            except Exception as e:
                customtkinter.CTkMessagebox.show_error("Error", f"Failed to upload image: {str(e)}")

    def run_simulation_event(self):
        # Initialize the font
        font = cv2.FONT_HERSHEY_PLAIN

        # Set up the webcam
        width = 640
        height = 360
        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        cam.set(cv2.CAP_PROP_FPS, 30)
        cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

        # Load the known faces
        path = "FaceList"
        images = []
        recNames = []
        myList = os.listdir(path)
        print(myList)
        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            recNames.append(os.path.splitext(cl)[0])
        print(recNames)

        # Function to find encodings
        def findEncodings(images):
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = FR.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList

        encodeListKnown = findEncodings(images)
        print('Encoding Complete')

        # Start webcam feed
        while True:
            ret, unknownFace = cam.read()
            if not ret:
                continue

            unknownFaceRGB = cv2.cvtColor(unknownFace, cv2.COLOR_BGR2RGB)
            faceLocations = FR.face_locations(unknownFaceRGB)
            unknownEncodings = FR.face_encodings(unknownFaceRGB, faceLocations)

            for faceLocation, unknownEncoding in zip(faceLocations, unknownEncodings):
                top, right, bottom, left = faceLocation
                print(faceLocation)

                name = 'Unknown Person'
                matches = FR.compare_faces(encodeListKnown, unknownEncoding)
                face_distances = FR.face_distance(encodeListKnown, unknownEncoding)
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    name = recNames[best_match_index]
                    box_color = (0, 255, 0)  # Green color for recognized faces
                else:
                    box_color = (0, 0, 255)  # Red color for unrecognized faces

                # Draw rectangle around the face
                cv2.rectangle(unknownFace, (left, top), (right, bottom), box_color, 3)

                # Put text above the rectangle
                cv2.putText(unknownFace, name, (left + 6, top - 6), font, 3, (0, 0, 255), 4)

            cv2.imshow('My Faces', unknownFace)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cam.release()
        cv2.destroyAllWindows()

# Inisialisasi aplikasi dan menjalankan loop utama
if __name__ == "__main__":
    app = App()
    app.mainloop()
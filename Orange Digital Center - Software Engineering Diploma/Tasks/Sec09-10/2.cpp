#include <iostream>
using namespace std;

class student {
	string name;
	int GPA;
	static string calc_GPA(int gpa) {
		if (GPA <= 100 && GPA > 85) {
			return "A";
		}
		else if (GPA <= 85 && GPA > 70) {
			return "B";
		}
		else if (GPA <= 70 && GPA > 60) {
			return "C";
		}
		else if (GPA <= 60 && GPA > 45) {
			return "D";
		}
	}
public:
	int phone;

	void set_name(string n) {
		name = n;
	}
	void set_GPA(int g) {
		GPA = g;
	}
	string get_name() {
		return name;
	}
	string get_GPA() {
		if (GPA <= 100 && GPA > 85) {
			return "A";
		}
		else if (GPA <= 85 && GPA > 70) {
			return "B";
		}
		else if (GPA <= 70 && GPA > 60) {
			return "C";
		}
		else if (GPA <= 60 && GPA > 45) {
			return "D";
		}
	}
	void get_phone() {
		cout << phone;
	}
};


int main() {
    student s1, s2, s3;
    string n;
    int g;

    // Student Number 1
    cout << "Enter Student Name: ";
    cin >> n;
    cout << "Enter Student GPA: ";
    cin >> g;
    cout << "Enter Student PhoneNumber: ";
    cin >> s1.phone;
    s1.set_name(n);
    s1.set_GPA(g);

    // Student Number 2
    cout << "Enter Student Name: ";
    cin >> n;
    cout << "Enter Student GPA: ";
    cin >> g;
    cout << "Enter Student PhoneNumber: ";
    cin >> s2.phone;
    s2.set_name(n);
    s2.set_GPA(g);

    // Student Number 3
    cout << "Enter Student Name: ";
    cin >> n;
    cout << "Enter Student GPA: ";
    cin >> g;
    cout << "Enter Student PhoneNumber: ";
    cin >> s3.phone;
    s3.set_name(n);
    s3.set_GPA(g);

    string s1_name = s1.get_name();
    string s2_name = s2.get_name();
    string s3_name = s3.get_name();

    string s1_GPA = s1.get_GPA();
    string s2_GPA = s2.get_GPA();
    string s3_GPA = s3.get_GPA();

    cout << "Student Name: " << s1_name << " | " << "GPA: " << s1_GPA << endl;
    cout << "Student Name: " << s2_name << " | " << "GPA: " << s2_GPA << endl;
    cout << "Student Name: " << s3_name << " | " << "GPA: " << s3_GPA;

    return 0;
}

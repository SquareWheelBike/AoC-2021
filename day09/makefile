JAVAC = javac
JVM = java
PYTHON = python3

JAVAC_FLAGS = -g

NAME = AoC
MAIN = input.txt
TEST = small.txt

.SUFFIXES : .class .java .py

# compile all .java files in src/
java: 
	$(JAVAC) $(JAVAC_FLAGS) *.java 
	$(JVM) $(NAME) $(MAIN)

# just run the main class
jtest:
	$(JAVAC) $(JAVAC_FLAGS) *.java 
	$(JVM) $(NAME) $(TEST)

py:
	$(PYTHON) $(NAME).py $(MAIN)

pytest:
	$(PYTHON) $(NAME).py $(TEST)

# clean the bin directory
# remove any serialized data
clean:
	rm -rf *.class

.PHONY: java jtest py pytest clean
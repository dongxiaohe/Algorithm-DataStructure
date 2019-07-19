import java.util.concurrent.Semaphore;

class Foo {

	Semaphore semaphoreSecond, semaphoreThird;

    public Foo() {
		semaphoreSecond = new Semaphore(0);       
		semaphoreThird = new Semaphore(0);        
    }

    public void first(Runnable printFirst) throws InterruptedException {
        printFirst.run();
		semaphoreSecond.release();
    }

    public void second(Runnable printSecond) throws InterruptedException {
		semaphoreSecond.acquire();
        printSecond.run();
		semaphoreThird.release();
    }

    public void third(Runnable printThird) throws InterruptedException {
		semaphoreThird.acquire();
        printThird.run();
    }
}

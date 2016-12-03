import XCTest
@testable import sweeper

class sweeperTests: XCTestCase {
    func testExample() {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        XCTAssertEqual(sweeper().text, "Hello, World!")
    }


    static var allTests : [(String, (sweeperTests) -> () throws -> Void)] {
        return [
            ("testExample", testExample),
        ]
    }
}

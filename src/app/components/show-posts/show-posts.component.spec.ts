import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowPostsComponent } from './show-posts.component';

describe('ShowPostsComponent', () => {
  let component: ShowPostsComponent;
  let fixture: ComponentFixture<ShowPostsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ShowPostsComponent]
    });
    fixture = TestBed.createComponent(ShowPostsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
